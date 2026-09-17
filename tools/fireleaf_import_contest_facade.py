#!/usr/bin/env python3
"""Import Emerald's Contest Hall facade into Vermilion's FRLG tileset."""

from pathlib import Path
import json
import re
import struct

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
VERMILION = ROOT / "data/tilesets/secondary/vermilion_city_frlg"
LILYCOVE = ROOT / "data/tilesets/secondary/lilycove"
EMERALD_PRIMARY = ROOT / "data/tilesets/primary/general"

# Seven by seven facade used by the Emerald Contest Hall in Lilycove.
FACADE = (
    (0x2C0, 0x2C1, 0x2C1, 0x2C1, 0x2C1, 0x2C1, 0x2C2),
    (0x2C8, 0x2C9, 0x2C9, 0x2C9, 0x2C9, 0x2C9, 0x2CA),
    (0x2C8, 0x2C9, 0x2C9, 0x2C9, 0x2C9, 0x2C9, 0x2CA),
    (0x2C8, 0x2C9, 0x2C9, 0x2C9, 0x2C9, 0x2C9, 0x2CA),
    (0x2D0, 0x2D1, 0x2D1, 0x2D1, 0x2D1, 0x2D1, 0x2D2),
    (0x2D8, 0x2D9, 0x2DA, 0x1D3, 0x2DB, 0x2D9, 0x2DC),
    (0x2E0, 0x2E1, 0x2E2, 0x1DB, 0x2E3, 0x2E1, 0x2E4),
)


def read_u16(path):
    raw = path.read_bytes()
    return list(struct.unpack(f"<{len(raw) // 2}H", raw))


def write_u16(path, values):
    path.write_bytes(struct.pack(f"<{len(values)}H", *values))


def write_palette(path, colors):
    text = "JASC-PAL\n0100\n16\n" + "\n".join("%d %d %d" % c for c in colors) + "\n"
    path.write_text(text)


def tile_from_sheet(sheet, tile_id):
    local_id = tile_id % 512
    x = (local_id % 16) * 8
    y = (local_id // 16) * 8
    return sheet.crop((x, y, x + 8, y + 8))


def main():
    dst_metatiles = read_u16(VERMILION / "metatiles.bin")
    dst_attrs_raw = (VERMILION / "metatile_attributes.bin").read_bytes()
    if len(dst_metatiles) != 168 * 8 or len(dst_attrs_raw) != 168 * 4:
        raise SystemExit("Vermilion tileset already changed; refusing a second facade import")

    dst_sheet = Image.open(VERMILION / "tiles.png").convert("P")
    if dst_sheet.size != (128, 72):
        raise SystemExit("Unexpected Vermilion tile sheet size")
    lily_sheet = Image.open(LILYCOVE / "tiles.png").convert("P")
    primary_sheet = Image.open(EMERALD_PRIMARY / "tiles.png").convert("P")
    lily_metatiles = read_u16(LILYCOVE / "metatiles.bin")
    primary_metatiles = read_u16(EMERALD_PRIMARY / "metatiles.bin")

    # These preserve Emerald's color roles while using FireRed's brighter
    # whites, stronger outlines, cooler roof blues and deeper wall reds.
    palette_13 = [
        (0, 0, 0), (246, 246, 255), (205, 222, 238), (172, 189, 205),
        (148, 164, 180), (123, 123, 131), (90, 90, 115), (65, 74, 106),
        (41, 49, 90), (156, 213, 255), (115, 189, 246), (255, 205, 139),
        (238, 148, 115), (222, 106, 98), (172, 32, 41), (115, 205, 164),
    ]
    palette_14 = [
        (0, 0, 0), (189, 255, 139), (131, 213, 98), (57, 148, 49),
        (57, 90, 16), (238, 148, 115), (106, 90, 90), (164, 98, 90),
        (65, 57, 49), (255, 205, 139), (222, 106, 98), (172, 32, 41),
        (164, 230, 197), (115, 205, 164), (65, 180, 139), (24, 164, 106),
    ]
    write_palette(VERMILION / "palettes/13.pal", palette_13)
    write_palette(VERMILION / "palettes/14.pal", palette_14)

    # The FRLG sheet currently has 144 secondary tiles. Append only the
    # distinct facade tiles, retaining flips from the original entries.
    imported = {}
    appended = []

    def import_entry(entry, source_sheet):
        source_tile = entry & 0x3FF
        source_palette = (entry >> 12) & 0xF
        key = ("primary" if source_sheet is primary_sheet else "secondary", source_tile)
        if key not in imported:
            imported[key] = 640 + 144 + len(appended)
            appended.append(tile_from_sheet(source_sheet, source_tile))
        palette = 13 if source_palette == 1 else 14
        return imported[key] | (entry & 0xC00) | (palette << 12)

    base_ground = read_u16(ROOT / "data/tilesets/primary/general_frlg/metatiles.bin")[8:12]
    source_to_custom = {}
    ordered_source_ids = []
    for row in FACADE:
        for source_id in row:
            if source_id not in source_to_custom:
                source_to_custom[source_id] = 640 + 168 + len(ordered_source_ids)
                ordered_source_ids.append(source_id)

    new_metatiles = []
    new_attrs = []
    for source_id in ordered_source_ids:
        if source_id >= 512:
            entries = lily_metatiles[(source_id - 512) * 8:(source_id - 512 + 1) * 8]
            overlay = [import_entry(entry, lily_sheet) if (entry & 0x3FF) else 0 for entry in entries[4:8]]
        else:
            entries = primary_metatiles[source_id * 8:(source_id + 1) * 8]
            # The two door blocks store their visible pixels in Emerald's
            # lower layer. Move them to FRLG's overlay layer.
            overlay = [import_entry(entry, primary_sheet) if (entry & 0x3FF) else 0 for entry in entries[0:4]]
        new_metatiles.extend(base_ground + overlay)
        behavior = 0x69 if source_id == 0x1DB else 0
        new_attrs.append(behavior | (2 << 29))  # split: ground below, facade above

    # Expand the indexed sheet in complete rows of sixteen 8x8 tiles.
    rows = (len(appended) + 15) // 16
    expanded = Image.new("P", (128, dst_sheet.height + rows * 8), 0)
    expanded.putpalette(dst_sheet.getpalette())
    expanded.paste(dst_sheet, (0, 0))
    for i, tile in enumerate(appended):
        expanded.paste(tile, ((i % 16) * 8, dst_sheet.height + (i // 16) * 8))
    expanded.save(VERMILION / "tiles.png", optimize=False)

    write_u16(VERMILION / "metatiles.bin", dst_metatiles + new_metatiles)
    old_attrs = list(struct.unpack(f"<{len(dst_attrs_raw) // 4}I", dst_attrs_raw))
    (VERMILION / "metatile_attributes.bin").write_bytes(
        struct.pack(f"<{len(old_attrs) + len(new_attrs)}I", *(old_attrs + new_attrs))
    )

    layouts = json.loads((ROOT / "data/layouts/layouts.json").read_text())["layouts"]
    layout = next(item for item in layouts if item["id"] == "LAYOUT_VERMILION_CITY")
    map_path = ROOT / layout["blockdata_filepath"]
    blocks = read_u16(map_path)
    width = layout["width"]
    dest_x, dest_y = 33, 5
    for y, row in enumerate(FACADE):
        for x, source_id in enumerate(row):
            collision = 0x400 if y else 0
            elevation = 0x3000 if y == 0 else 0
            blocks[(dest_y + y) * width + dest_x + x] = source_to_custom[source_id] | collision | elevation
    write_u16(map_path, blocks)


if __name__ == "__main__":
    main()
