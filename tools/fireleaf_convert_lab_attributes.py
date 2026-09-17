#!/usr/bin/env python3
"""Apply Fireleaf's reproducible map adjustments."""

from pathlib import Path
import struct


# The lab uses the native FireRed u32 attribute table.  Do not attempt to
# expand the old 350-byte file entry-by-entry: it was truncated/mispacked and
# doing so changes tile ordering, hiding the starter balls and breaking doors.
attribute_path = Path("data/tilesets/secondary/lab_frlg/metatile_attributes.bin")
if attribute_path.stat().st_size != 700:
    raise SystemExit("Oak's lab must use the complete 700-byte FireRed attribute table")

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
