#!/usr/bin/env python3
"""Convert the accidentally imported Emerald lab attributes to FRLG format."""

from pathlib import Path
import struct


path = Path("data/tilesets/secondary/lab_frlg/metatile_attributes.bin")
raw = path.read_bytes()

if len(raw) == 350:
    emerald_attrs = struct.unpack(f"<{len(raw) // 2}H", raw)
    frlg_attrs = []
    for attr in emerald_attrs:
        behavior = attr & 0x1FF
        layer_type = (attr >> 12) & 0x3
        frlg_attrs.append(behavior | (layer_type << 29))
    path.write_bytes(struct.pack(f"<{len(frlg_attrs)}I", *frlg_attrs))
elif len(raw) != 700:
    raise SystemExit(f"Unexpected lab attribute size: {len(raw)}")

# Replace Vermilion's construction lot with the existing four-by-four Gen III
# shop facade. The facade's door (third tile of the bottom row) lines up with
# the Contest Lobby warp declared in the map JSON.
map_path = Path("data/layouts/VermilionCity_Frlg/map.bin")
map_raw = map_path.read_bytes()
blocks = list(struct.unpack(f"<{len(map_raw) // 2}H", map_raw))
width = 48
source_x, source_y = 27, 14
dest_x, dest_y = 34, 8
facade = [
    blocks[(source_y + y) * width + source_x:(source_y + y) * width + source_x + 4]
    for y in range(4)
]
for y, row in enumerate(facade):
    start = (dest_y + y) * width + dest_x
    blocks[start:start + 4] = row
map_path.write_bytes(struct.pack(f"<{len(blocks)}H", *blocks))
