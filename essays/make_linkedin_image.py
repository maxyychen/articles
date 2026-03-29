#!/usr/bin/env python3
"""Recreate change_lifecycle.png at LinkedIn-optimized dimensions."""

from PIL import Image, ImageDraw, ImageFont

# --- Config ---
W, H = 1080, 1350  # 4:5 ratio, optimal for LinkedIn feed
BOX_W = 340
BOX_H = 90
BOX_RADIUS = 16
ARROW_WIDTH = 4

# Colors - modern professional palette
BG_COLOR = "#F7F7F2"
BOX_COLOR = "#5B2C6F"
BOX_TEXT_COLOR = "#FFFFFF"
ARROW_COLOR = "#5B2C6F"
LOOP_COLOR = "#2E86C1"
TITLE_COLOR = "#2C3E50"

# Fonts
FONT_PATH = "/System/Library/Fonts/Avenir Next.ttc"
font_box = ImageFont.truetype(FONT_PATH, size=30, index=2)       # Demi Bold
font_loop = ImageFont.truetype(FONT_PATH, size=26, index=2)      # Demi Bold smaller
font_title = ImageFont.truetype(FONT_PATH, size=52, index=0)     # Bold
font_sub = ImageFont.truetype(FONT_PATH, size=24, index=5)       # Medium
font_badge = ImageFont.truetype(FONT_PATH, size=20, index=0)     # Bold small

# Steps
steps = [
    "What is the vision?",
    "Where are we now?",
    "Where do we want to be?",
    "How do we get there?",
    "Take action",
    "Did we get there?",
]
loop_label = "How do we keep\nthe momentum going?"

# --- Layout ---
img = Image.new("RGB", (W, H), BG_COLOR)
draw = ImageDraw.Draw(img)

# Title
title_y = 65
draw.text((W // 2, title_y), "Change Lifecycle", anchor="mt", font=font_title, fill=TITLE_COLOR)
draw.text((W // 2, title_y + 62), "A framework for sustainable transformation", anchor="mt", font=font_sub, fill="#7F8C8D")

# Main flow: right side of canvas
flow_x = 660
top_y = 210
gap_y = 155
box_positions = [(flow_x, top_y + i * gap_y + BOX_H // 2) for i in range(len(steps))]

# Loop box: left side
loop_cx = 220
last_cy = box_positions[-1][1]
first_cy = box_positions[0][1]
loop_cy = (last_cy + first_cy) // 2 + 60
LOOP_BOX_W = 320
LOOP_BOX_H = 110


def draw_box(cx, cy, text, color=BOX_COLOR, w=BOX_W, h=BOX_H, font=font_box):
    x0, y0 = cx - w // 2, cy - h // 2
    x1, y1 = cx + w // 2, cy + h // 2
    # Shadow
    draw.rounded_rectangle((x0 + 4, y0 + 4, x1 + 4, y1 + 4), radius=BOX_RADIUS, fill="#D5D5D0")
    draw.rounded_rectangle((x0, y0, x1, y1), radius=BOX_RADIUS, fill=color)
    draw.text((cx, cy), text, anchor="mm", font=font, fill=BOX_TEXT_COLOR)


def arrow_down(x, y1, y2, color=ARROW_COLOR):
    hl = 12
    draw.line([(x, y1), (x, y2 - hl)], fill=color, width=ARROW_WIDTH)
    draw.polygon([(x, y2), (x - hl, y2 - hl), (x + hl, y2 - hl)], fill=color)


# --- Draw feedback loop path first (behind boxes) ---
lc = LOOP_COLOR

# Down from last box
bottom_y = last_cy + BOX_H // 2
turn_y = bottom_y + 50
draw.line([(flow_x, bottom_y), (flow_x, turn_y)], fill=lc, width=ARROW_WIDTH)

# Left to loop column
draw.line([(flow_x, turn_y), (loop_cx, turn_y)], fill=lc, width=ARROW_WIDTH)

# Up to loop box bottom
draw.line([(loop_cx, turn_y), (loop_cx, loop_cy + LOOP_BOX_H // 2)], fill=lc, width=ARROW_WIDTH)

# Loop box
draw_box(loop_cx, loop_cy, loop_label, color=LOOP_COLOR, w=LOOP_BOX_W, h=LOOP_BOX_H, font=font_loop)

# Up from loop box top
top_turn_y = first_cy - 50
draw.line([(loop_cx, loop_cy - LOOP_BOX_H // 2), (loop_cx, top_turn_y)], fill=lc, width=ARROW_WIDTH)

# Right to flow column
draw.line([(loop_cx, top_turn_y), (flow_x, top_turn_y)], fill=lc, width=ARROW_WIDTH)

# Down into first box
arrow_down(flow_x, top_turn_y, first_cy - BOX_H // 2, color=lc)

# --- Draw arrows between main boxes ---
for i in range(len(steps) - 1):
    _, cy1 = box_positions[i]
    _, cy2 = box_positions[i + 1]
    arrow_down(flow_x, cy1 + BOX_H // 2, cy2 - BOX_H // 2)

# --- Draw main flow boxes ---
for i, step in enumerate(steps):
    cx, cy = box_positions[i]
    draw_box(cx, cy, step)

# Number badges
for i in range(len(steps)):
    cx, cy = box_positions[i]
    bx = cx - BOX_W // 2 + 6
    by = cy - BOX_H // 2 + 6
    br = 16
    draw.ellipse((bx, by, bx + br * 2, by + br * 2), fill="#F39C12")
    draw.text((bx + br, by + br), str(i + 1), anchor="mm", font=font_badge, fill="#FFFFFF")

# Footer
draw.text((W // 2, H - 50), "Continuous improvement through iterative change", anchor="mm", font=font_sub, fill="#95A5A6")

# Save
out = "/Users/chenyuyu/work/articles/essays/change_lifecycle_linkedin.png"
img.save(out, "PNG", dpi=(144, 144))
print(f"Saved: {W}x{H}")
