from PIL import Image, ImageDraw, ImageFont

# Set up canvas
width, height = 800, 400
bg_color = (255, 250, 240)  # Floral White (warm)
image = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(image)

# Colors
req_color = (255, 182, 193)    # Light Pink
arch_color = (135, 206, 250)   # Light Sky Blue
code_color = (144, 238, 144)   # Light Green
arrow_color = (105, 105, 105)  # Dim Gray
text_color = (50, 50, 50)

# Cartoon style helper: rounded rectangles with "hand-drawn" feel (jittered lines)
def draw_bubble(draw, xy, color, label):
    x0, y0, x1, y1 = xy
    # Draw main shape
    draw.rounded_rectangle(xy, radius=20, fill=color, outline=text_color, width=4)
    # Add a shadow for cartoon feel
    draw.text(((x0+x1)/2, (y0+y1)/2), label, fill=text_color, anchor="mm")

# Define positions
margin = 50
bubble_w = 180
bubble_h = 100
y_mid = height // 2 - bubble_h // 2

req_box = [margin, y_mid, margin + bubble_w, y_mid + bubble_h]
arch_box = [width//2 - bubble_w//2, y_mid, width//2 + bubble_w//2, y_mid + bubble_h]
code_box = [width - margin - bubble_w, y_mid, width - margin, y_mid + bubble_h]

# Draw Arrows
def draw_arrow(draw, start, end):
    draw.line([start, end], fill=arrow_color, width=6)
    # Arrow head
    x, y = end
    draw.polygon([(x, y), (x-15, y-10), (x-15, y+10)], fill=arrow_color)

# Execute Drawing
draw_bubble(draw, req_box, req_color, "📝 Requirements")
draw_bubble(draw, arch_box, arch_color, "🏗️ ARCHITECTURE\n(The Missing Middle)")
draw_bubble(draw, code_box, code_color, "💻 Code")

# Connect them
draw_arrow(draw, (req_box[2]+5, height//2), (arch_box[0]-5, height//2))
draw_arrow(draw, (arch_box[2]+5, height//2), (code_box[0]-5, height//2))

# Title
draw.text((width//2, 50), "AI Development: The Healthy Path", fill=text_color, anchor="mm")

# Save
image.save("ai_architecture_diagram.png")
