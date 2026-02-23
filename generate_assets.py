#!/usr/bin/env python3
"""
Pixel art asset generator for Furrball Collector game.
Generates 32x32 pixel art PNGs for cats, furballs, and gacha items.
"""

from PIL import Image, ImageDraw

# ============================================================
# Helper
# ============================================================

def new_sprite(size=32):
    """Create a new transparent RGBA image."""
    return Image.new("RGBA", (size, size), (0, 0, 0, 0))


def put_pixels(img, pixel_map):
    """
    Draw pixels from a dict of {(x, y): (r, g, b, a)} or {(x, y): (r, g, b)}.
    """
    for (x, y), color in pixel_map.items():
        if len(color) == 3:
            color = (*color, 255)
        if 0 <= x < img.width and 0 <= y < img.height:
            img.putpixel((x, y), color)
    return img


def fill_rect(img, x0, y0, x1, y1, color):
    """Fill a rectangle on the image."""
    if len(color) == 3:
        color = (*color, 255)
    draw = ImageDraw.Draw(img)
    draw.rectangle([x0, y0, x1, y1], fill=color)
    return img


def draw_outline(img, x0, y0, x1, y1, color):
    """Draw rectangle outline."""
    if len(color) == 3:
        color = (*color, 255)
    draw = ImageDraw.Draw(img)
    draw.rectangle([x0, y0, x1, y1], outline=color)
    return img


# ============================================================
# CATS  (32x32 side-view walking pose)
# ============================================================

def make_cat(body_color, stripe_color=None, eye_color=(50, 205, 50),
             belly_color=None, name="cat"):
    """
    Generate a 32x32 pixel art cat sprite (side-view, walking).
    """
    img = new_sprite(32)

    bc = body_color
    sc = stripe_color or body_color
    ec = eye_color
    blc = belly_color or tuple(min(c + 60, 255) for c in body_color)
    outline = (40, 40, 40)
    nose = (255, 150, 150)
    inner_ear = (255, 180, 180)

    # --- Body (main oval area) ---
    # Body core: rows 14-22, cols 8-24
    for y in range(14, 23):
        for x in range(8, 25):
            img.putpixel((x, y), (*bc, 255))

    # Body top curve
    for x in range(10, 23):
        img.putpixel((x, 13), (*bc, 255))
    for x in range(12, 21):
        img.putpixel((x, 12), (*bc, 255))

    # Body bottom curve
    for x in range(10, 23):
        img.putpixel((x, 23), (*bc, 255))

    # Belly
    for y in range(19, 23):
        for x in range(11, 22):
            img.putpixel((x, y), (*blc, 255))

    # --- Stripes (if provided) ---
    if stripe_color and stripe_color != body_color:
        for y in range(14, 20):
            for x in [11, 15, 19, 23]:
                if 0 <= x < 32 and 0 <= y < 32:
                    img.putpixel((x, y), (*sc, 255))
                    if x + 1 < 32:
                        img.putpixel((x + 1, y), (*sc, 255))

    # --- Head ---
    # Head: rows 6-14, cols 18-29
    for y in range(7, 15):
        for x in range(19, 29):
            img.putpixel((x, y), (*bc, 255))
    for x in range(20, 28):
        img.putpixel((x, 6), (*bc, 255))
    for x in range(21, 27):
        img.putpixel((x, 5), (*bc, 255))

    # --- Ears ---
    # Left ear
    for i in range(4):
        img.putpixel((20 - i, 5 - i), (*bc, 255))
        img.putpixel((21 - i, 5 - i), (*bc, 255))
    img.putpixel((20, 4), (*inner_ear, 255))

    # Right ear
    for i in range(4):
        img.putpixel((26 + i, 5 - i), (*bc, 255))
        img.putpixel((27 + i, 5 - i), (*bc, 255))
    img.putpixel((27, 4), (*inner_ear, 255))

    # --- Face ---
    # Eyes
    img.putpixel((22, 9), (*ec, 255))
    img.putpixel((23, 9), (*ec, 255))
    img.putpixel((26, 9), (*ec, 255))
    img.putpixel((27, 9), (*ec, 255))
    # Pupils
    img.putpixel((23, 9), (20, 20, 20, 255))
    img.putpixel((27, 9), (20, 20, 20, 255))

    # Nose
    img.putpixel((24, 11), (*nose, 255))
    img.putpixel((25, 11), (*nose, 255))

    # Mouth
    img.putpixel((23, 12), (*outline, 255))
    img.putpixel((24, 13), (*outline, 255))
    img.putpixel((25, 13), (*outline, 255))
    img.putpixel((26, 12), (*outline, 255))

    # Whiskers
    for dx in range(4):
        img.putpixel((18 - dx, 10), (*outline, 255))
        img.putpixel((18 - dx, 12), (*outline, 255))

    # --- Tail ---
    # Curved tail from back of body going up
    tail_pixels = [
        (7, 16), (6, 15), (5, 14), (4, 13), (3, 12),
        (3, 11), (4, 10), (5, 9), (6, 9), (7, 10),
    ]
    for (x, y) in tail_pixels:
        img.putpixel((x, y), (*bc, 255))
        img.putpixel((x, y + 1), (*bc, 255))

    # Tail tip
    img.putpixel((6, 8), (*bc, 255))
    img.putpixel((7, 9), (*bc, 255))

    # --- Legs ---
    leg_color = bc
    # Front legs
    for y in range(23, 29):
        img.putpixel((21, y), (*leg_color, 255))
        img.putpixel((22, y), (*leg_color, 255))
        img.putpixel((18, y), (*leg_color, 255))
        img.putpixel((19, y), (*leg_color, 255))

    # Back legs
    for y in range(23, 29):
        img.putpixel((12, y), (*leg_color, 255))
        img.putpixel((13, y), (*leg_color, 255))
        img.putpixel((9, y), (*leg_color, 255))
        img.putpixel((10, y), (*leg_color, 255))

    # Paws
    paw_color = blc
    for x_base in [9, 12, 18, 21]:
        img.putpixel((x_base, 29), (*paw_color, 255))
        img.putpixel((x_base + 1, 29), (*paw_color, 255))
        img.putpixel((x_base - 1, 29), (*paw_color, 255))

    # --- Outline (simple border pass) ---
    outlined = add_outline(img, outline)

    return outlined


def add_outline(img, outline_color=(40, 40, 40)):
    """Add a 1px dark outline around non-transparent pixels."""
    result = img.copy()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if img.getpixel((x, y))[3] == 0:
                # Check neighbors
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        if img.getpixel((nx, ny))[3] > 0:
                            result.putpixel((x, y), (*outline_color, 255))
                            break
    return result


# ============================================================
# FURBALLS
# ============================================================

def make_furball(color, size_variant="medium", name="furball"):
    """Generate a fluffy fur ball sprite."""
    img = new_sprite(32)

    if size_variant == "small":
        cx, cy, r = 16, 20, 4
    elif size_variant == "medium":
        cx, cy, r = 16, 18, 6
    else:  # large
        cx, cy, r = 16, 16, 8

    # Draw fuzzy circle
    lighter = tuple(min(c + 40, 255) for c in color)
    darker = tuple(max(c - 40, 0) for c in color)

    for y in range(32):
        for x in range(32):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if dist <= r:
                img.putpixel((x, y), (*color, 255))
            elif dist <= r + 1.5:
                # Fuzzy edge - alternating pixels for fluffiness
                if (x + y) % 2 == 0:
                    img.putpixel((x, y), (*color, 200))

    # Add fluffy texture
    import random
    random.seed(hash(name))
    for _ in range(r * 6):
        angle = random.random() * 6.28
        dist = random.random() * r
        fx = int(cx + dist * __import__('math').cos(angle))
        fy = int(cy + dist * __import__('math').sin(angle))
        if 0 <= fx < 32 and 0 <= fy < 32:
            if random.random() > 0.5:
                img.putpixel((fx, fy), (*lighter, 255))
            else:
                img.putpixel((fx, fy), (*darker, 255))

    # Add some stray fur strands
    for _ in range(8):
        angle = random.random() * 6.28
        for d in range(r, r + 3):
            sx = int(cx + d * __import__('math').cos(angle))
            sy = int(cy + d * __import__('math').sin(angle))
            if 0 <= sx < 32 and 0 <= sy < 32:
                img.putpixel((sx, sy), (*color, 180))

    # Sparkle effect (it's currency!)
    sparkle = (255, 255, 220)
    sparkle_positions = [(cx - r + 2, cy - r + 2), (cx + r - 3, cy - r + 1)]
    for sx, sy in sparkle_positions:
        if 0 <= sx < 32 and 0 <= sy < 32:
            img.putpixel((sx, sy), (*sparkle, 255))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = sx + dx, sy + dy
                if 0 <= nx < 32 and 0 <= ny < 32:
                    img.putpixel((nx, ny), (*sparkle, 180))

    return img


# ============================================================
# GACHA ITEMS
# ============================================================

def make_traffic_cone():
    """Generate a pixel art traffic cone (라바콘)."""
    img = new_sprite(32)
    outline = (40, 40, 40)
    orange = (255, 140, 0)
    white_stripe = (255, 255, 255)
    base_color = (80, 80, 80)

    # Base
    fill_rect(img, 8, 27, 24, 30, base_color)
    fill_rect(img, 7, 28, 25, 30, base_color)

    # Cone body (trapezoid)
    for row in range(0, 20):
        y = 27 - row
        half_width = int(8 - row * 0.35)
        x0 = 16 - half_width
        x1 = 16 + half_width
        if x0 < x1:
            fill_rect(img, x0, y, x1, y, orange)

    # White reflective stripes
    for row_start in [4, 11]:
        for row in range(row_start, row_start + 3):
            y = 27 - row
            half_width = int(8 - row * 0.35)
            x0 = 16 - half_width + 1
            x1 = 16 + half_width - 1
            if x0 < x1 and 0 <= y < 32:
                fill_rect(img, x0, y, x1, y, white_stripe)

    # Tip
    img.putpixel((16, 7), (*orange, 255))
    img.putpixel((15, 7), (*orange, 255))
    img.putpixel((16, 6), (*orange, 255))

    return add_outline(img, outline)


def make_cat_tower():
    """Generate a pixel art cat tower (캣타워)."""
    img = new_sprite(32)
    outline = (40, 40, 40)
    wood = (160, 120, 60)
    wood_dark = (130, 95, 45)
    carpet = (180, 140, 100)
    carpet_dark = (150, 110, 75)
    platform = (200, 170, 130)

    # Base platform
    fill_rect(img, 6, 28, 26, 30, platform)

    # Center pole
    fill_rect(img, 14, 5, 18, 28, wood)
    fill_rect(img, 15, 5, 17, 28, wood_dark)

    # Sisal rope texture on pole
    for y in range(6, 28, 2):
        fill_rect(img, 14, y, 18, y, carpet)

    # Bottom platform
    fill_rect(img, 4, 25, 28, 27, platform)
    fill_rect(img, 5, 24, 27, 25, carpet)

    # Middle platform
    fill_rect(img, 7, 16, 25, 18, platform)
    fill_rect(img, 8, 15, 24, 16, carpet)

    # Top platform (with raised edges like a bed)
    fill_rect(img, 5, 6, 27, 8, platform)
    fill_rect(img, 6, 5, 26, 6, carpet)
    fill_rect(img, 5, 4, 7, 6, carpet_dark)
    fill_rect(img, 25, 4, 27, 6, carpet_dark)

    # Small toy dangling from middle platform
    img.putpixel((24, 19), (*outline, 255))
    img.putpixel((24, 20), (*outline, 255))
    img.putpixel((23, 21), (255, 80, 80, 255))
    img.putpixel((24, 21), (255, 80, 80, 255))
    img.putpixel((25, 21), (255, 80, 80, 255))
    img.putpixel((24, 22), (255, 80, 80, 255))

    return add_outline(img, outline)


def make_trash_can():
    """Generate a pixel art trash can (쓰레기통)."""
    img = new_sprite(32)
    outline = (40, 40, 40)
    metal = (170, 175, 180)
    metal_dark = (140, 145, 150)
    metal_light = (200, 205, 210)
    lid = (150, 155, 160)

    # Can body
    fill_rect(img, 9, 12, 23, 29, metal)
    fill_rect(img, 10, 12, 14, 29, metal_dark)
    fill_rect(img, 19, 12, 22, 29, metal_light)

    # Horizontal ridges
    for y in [15, 19, 23, 27]:
        fill_rect(img, 9, y, 23, y, metal_dark)

    # Base
    fill_rect(img, 8, 29, 24, 30, metal_dark)

    # Lid
    fill_rect(img, 7, 10, 25, 12, lid)
    fill_rect(img, 8, 9, 24, 10, lid)

    # Handle on lid
    fill_rect(img, 14, 7, 18, 9, metal_dark)
    fill_rect(img, 15, 6, 17, 7, metal_dark)

    # Slight opening with trash peeking
    img.putpixel((24, 10), (0, 0, 0, 0))
    img.putpixel((25, 10), (0, 0, 0, 0))
    # Fish bone peeking out
    img.putpixel((24, 9), (230, 230, 220, 255))
    img.putpixel((25, 9), (230, 230, 220, 255))
    img.putpixel((26, 9), (230, 230, 220, 255))
    img.putpixel((25, 8), (230, 230, 220, 255))

    return add_outline(img, outline)


def make_yarn_ball():
    """Generate a pixel art yarn ball (털실 뭉치)."""
    img = new_sprite(32)
    yarn_color = (220, 60, 80)
    yarn_light = (240, 100, 120)
    yarn_dark = (180, 40, 60)

    cx, cy, r = 16, 16, 8

    # Base circle
    for y in range(32):
        for x in range(32):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if dist <= r:
                img.putpixel((x, y), (*yarn_color, 255))

    # Yarn wrap lines (curved)
    import math
    for angle_offset in [0, 1.2, 2.4, 3.6, 4.8]:
        for t in range(60):
            a = angle_offset + t * 0.15
            rx = int(cx + (r - 1) * math.cos(a) * math.sin(t * 0.1))
            ry = int(cy + (r - 1) * math.sin(a))
            if 0 <= rx < 32 and 0 <= ry < 32:
                dist = ((rx - cx) ** 2 + (ry - cy) ** 2) ** 0.5
                if dist <= r:
                    img.putpixel((rx, ry), (*yarn_light, 255))

    # Shading
    for y in range(32):
        for x in range(32):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if r - 2 < dist <= r:
                if x > cx and y > cy:
                    px = img.getpixel((x, y))
                    if px[3] > 0:
                        img.putpixel((x, y), (*yarn_dark, 255))

    # Trailing yarn string
    trail = [(cx + r + 1, cy + 2), (cx + r + 2, cy + 3), (cx + r + 3, cy + 5),
             (cx + r + 2, cy + 7), (cx + r + 3, cy + 9)]
    for (x, y) in trail:
        if 0 <= x < 32 and 0 <= y < 32:
            img.putpixel((x, y), (*yarn_color, 255))

    # Highlight
    img.putpixel((cx - 3, cy - 3), (255, 200, 210, 255))
    img.putpixel((cx - 2, cy - 4), (255, 220, 225, 255))

    return add_outline(img)


def make_fish_toy():
    """Generate a pixel art fish toy (물고기 장난감)."""
    img = new_sprite(32)
    body = (100, 180, 220)
    body_light = (140, 210, 240)
    body_dark = (70, 140, 180)
    fin = (80, 150, 200)
    eye_white = (255, 255, 255)
    eye_black = (20, 20, 20)

    # Body (oval)
    cx, cy = 15, 16
    for y in range(32):
        for x in range(32):
            # Ellipse: wider than tall
            dx = (x - cx) / 9
            dy = (y - cy) / 5
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*body, 255))

    # Upper shading
    for y in range(12, 15):
        for x in range(9, 22):
            dx = (x - cx) / 9
            dy = (y - cy) / 5
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*body_light, 255))

    # Lower shading
    for y in range(18, 22):
        for x in range(9, 22):
            dx = (x - cx) / 9
            dy = (y - cy) / 5
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*body_dark, 255))

    # Tail
    for i in range(5):
        fill_rect(img, 24 + i, 14 - i, 25 + i, 18 + i, fin)

    # Eye
    fill_rect(img, 9, 14, 11, 16, eye_white)
    img.putpixel((10, 15), (*eye_black, 255))

    # Mouth
    img.putpixel((6, 16), (*eye_black, 255))
    img.putpixel((7, 17), (*eye_black, 255))

    # Scales pattern
    for y in range(14, 20, 2):
        for x in range(12, 22, 3):
            dx = (x - cx) / 9
            dy = (y - cy) / 5
            if dx * dx + dy * dy <= 0.8:
                img.putpixel((x, y), (*body_light, 255))

    return add_outline(img)


def make_cardboard_box():
    """Generate a pixel art cardboard box (택배 상자)."""
    img = new_sprite(32)
    box = (190, 150, 90)
    box_dark = (160, 120, 65)
    box_light = (210, 175, 120)
    tape = (200, 180, 130)
    outline = (40, 40, 40)

    # Box body (3D-ish)
    fill_rect(img, 5, 12, 24, 28, box)
    fill_rect(img, 5, 12, 14, 28, box_dark)

    # Top face (parallelogram for 3D effect)
    fill_rect(img, 5, 8, 24, 12, box_light)

    # Flaps (open)
    fill_rect(img, 3, 5, 10, 9, box)
    fill_rect(img, 19, 4, 26, 9, box)

    # Tape on front
    fill_rect(img, 13, 12, 16, 28, tape)

    # Box texture lines
    fill_rect(img, 5, 20, 24, 20, box_dark)

    return add_outline(img, outline)


def make_cushion():
    """Generate a pixel art cushion/pillow (쿠션)."""
    img = new_sprite(32)
    fabric = (255, 180, 200)
    fabric_dark = (230, 150, 170)
    fabric_light = (255, 210, 220)

    # Rounded cushion shape
    cx, cy = 16, 18
    for y in range(32):
        for x in range(32):
            dx = (x - cx) / 11
            dy = (y - cy) / 7
            dist = dx * dx + dy * dy
            if dist <= 1:
                if dist > 0.7:
                    img.putpixel((x, y), (*fabric_dark, 255))
                elif dy < -0.3:
                    img.putpixel((x, y), (*fabric_light, 255))
                else:
                    img.putpixel((x, y), (*fabric, 255))

    # Corner tufts
    tufts = [(7, 13), (25, 13), (7, 23), (25, 23)]
    for tx, ty in tufts:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = tx + dx, ty + dy
                if 0 <= nx < 32 and 0 <= ny < 32:
                    img.putpixel((nx, ny), (*fabric_dark, 255))

    # Button in center
    img.putpixel((16, 18), (*fabric_dark, 255))
    img.putpixel((15, 18), (*fabric_dark, 255))
    img.putpixel((16, 17), (*fabric_dark, 255))
    img.putpixel((15, 17), (*fabric_dark, 255))

    return add_outline(img)


def make_food_bowl():
    """Generate a pixel art food bowl (밥그릇)."""
    img = new_sprite(32)
    bowl = (220, 80, 80)
    bowl_dark = (180, 60, 60)
    bowl_light = (240, 120, 120)
    food = (160, 120, 60)
    food_light = (180, 145, 80)
    inner = (240, 240, 235)

    # Bowl body (semi-ellipse)
    cx, cy = 16, 20
    for y in range(17, 29):
        for x in range(32):
            dx = (x - cx) / 11
            dy = (y - cy) / 8
            if dx * dx + dy * dy <= 1:
                if x < 13:
                    img.putpixel((x, y), (*bowl_dark, 255))
                elif x > 19:
                    img.putpixel((x, y), (*bowl_light, 255))
                else:
                    img.putpixel((x, y), (*bowl, 255))

    # Inner rim
    for x in range(8, 25):
        img.putpixel((x, 17), (*inner, 255))
        img.putpixel((x, 18), (*inner, 255))

    # Food inside
    for y in range(17, 21):
        for x in range(9, 24):
            dx = (x - cx) / 10
            dy = (y - 18) / 3
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*food, 255))

    # Food kibble texture
    for x in range(10, 23, 2):
        img.putpixel((x, 18), (*food_light, 255))
        if x + 1 < 23:
            img.putpixel((x + 1, 19), (*food_light, 255))

    # Paw print on bowl
    img.putpixel((16, 23), (*bowl_light, 255))
    img.putpixel((15, 22), (*bowl_light, 255))
    img.putpixel((17, 22), (*bowl_light, 255))
    img.putpixel((16, 21), (*bowl_light, 255))

    return add_outline(img)


def make_mouse_toy():
    """Generate a pixel art mouse toy (쥐 장난감)."""
    img = new_sprite(32)
    body = (180, 180, 180)
    body_dark = (150, 150, 150)
    ear = (255, 180, 180)
    eye = (20, 20, 20)
    nose = (255, 130, 130)
    tail = (200, 160, 160)

    # Body (small oval)
    cx, cy = 16, 19
    for y in range(32):
        for x in range(32):
            dx = (x - cx) / 7
            dy = (y - cy) / 5
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*body, 255))

    # Darker underside
    for y in range(21, 25):
        for x in range(10, 23):
            dx = (x - cx) / 7
            dy = (y - cy) / 5
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*body_dark, 255))

    # Ears
    for dy in range(-2, 1):
        for dx in range(-2, 1):
            img.putpixel((11 + dx, 14 + dy), (*ear, 255))
            img.putpixel((13 + dx, 13 + dy), (*body, 255))

    # Nose
    img.putpixel((9, 18), (*nose, 255))
    img.putpixel((8, 18), (*nose, 255))

    # Eye
    img.putpixel((11, 17), (*eye, 255))

    # Whiskers
    for dx in range(3):
        img.putpixel((7 - dx, 17), (*body_dark, 255))
        img.putpixel((7 - dx, 19), (*body_dark, 255))

    # Tail (curvy)
    tail_pts = [(23, 19), (24, 18), (25, 17), (26, 17), (27, 18),
                (28, 19), (29, 18), (30, 17)]
    for (x, y) in tail_pts:
        if 0 <= x < 32 and 0 <= y < 32:
            img.putpixel((x, y), (*tail, 255))

    return add_outline(img)


def make_plant_pot():
    """Generate a pixel art plant pot (화분)."""
    img = new_sprite(32)
    pot = (180, 100, 60)
    pot_dark = (150, 75, 40)
    pot_rim = (200, 120, 75)
    soil = (80, 60, 40)
    leaf = (60, 180, 80)
    leaf_dark = (40, 140, 55)

    # Pot body (trapezoid)
    for row in range(12):
        y = 30 - row
        half_w = 5 + int(row * 0.3)
        x0 = 16 - half_w
        x1 = 16 + half_w
        fill_rect(img, x0, y, x1, y, pot if row < 8 else pot_dark)

    # Pot rim
    fill_rect(img, 8, 18, 24, 20, pot_rim)

    # Soil
    fill_rect(img, 9, 17, 23, 18, soil)

    # Plant leaves
    # Center stem
    for y in range(8, 18):
        img.putpixel((16, y), (*leaf_dark, 255))

    # Leaves
    leaf_positions = [
        [(14, 10), (13, 9), (12, 8), (11, 8), (12, 9)],
        [(18, 10), (19, 9), (20, 8), (21, 8), (20, 9)],
        [(14, 13), (13, 12), (12, 12), (11, 13)],
        [(18, 13), (19, 12), (20, 12), (21, 13)],
        [(15, 7), (16, 6), (17, 7)],
    ]
    for positions in leaf_positions:
        for (x, y) in positions:
            if 0 <= x < 32 and 0 <= y < 32:
                img.putpixel((x, y), (*leaf, 255))

    return add_outline(img)


def make_scratching_post():
    """Generate a pixel art scratching post (스크래처)."""
    img = new_sprite(32)
    sisal = (200, 180, 140)
    sisal_dark = (170, 150, 110)
    base = (120, 100, 70)
    top_ball = (255, 80, 80)

    # Base
    fill_rect(img, 6, 27, 26, 30, base)

    # Post
    fill_rect(img, 13, 6, 19, 27, sisal)

    # Rope wrapping texture
    for y in range(7, 27, 2):
        fill_rect(img, 13, y, 19, y, sisal_dark)

    # Scratch marks
    img.putpixel((14, 12), (160, 140, 100, 255))
    img.putpixel((14, 14), (160, 140, 100, 255))
    img.putpixel((18, 18), (160, 140, 100, 255))
    img.putpixel((18, 20), (160, 140, 100, 255))

    # Top platform
    fill_rect(img, 10, 4, 22, 6, base)

    # Dangling ball
    img.putpixel((22, 7), (40, 40, 40, 255))
    img.putpixel((22, 8), (40, 40, 40, 255))
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            nx, ny = 22 + dx, 10 + dy
            if 0 <= nx < 32 and 0 <= ny < 32:
                img.putpixel((nx, ny), (*top_ball, 255))

    return add_outline(img)


def make_window_perch():
    """Generate a pixel art window perch/shelf (창문 선반)."""
    img = new_sprite(32)
    frame = (180, 160, 130)
    glass = (200, 220, 240)
    glass_light = (230, 240, 250)
    shelf = (160, 120, 70)
    cushion = (100, 140, 200)
    cushion_light = (130, 170, 230)

    # Window frame
    fill_rect(img, 4, 2, 28, 20, frame)
    fill_rect(img, 6, 4, 26, 18, glass)

    # Window reflection
    fill_rect(img, 7, 5, 12, 8, glass_light)

    # Window divider
    fill_rect(img, 15, 4, 17, 18, frame)
    fill_rect(img, 6, 10, 26, 12, frame)

    # Shelf/perch
    fill_rect(img, 2, 20, 30, 23, shelf)

    # Cushion on shelf
    for y in range(23, 28):
        for x in range(5, 27):
            dx = (x - 16) / 11
            dy = (y - 25) / 3
            if dx * dx + dy * dy <= 1:
                if y < 25:
                    img.putpixel((x, y), (*cushion_light, 255))
                else:
                    img.putpixel((x, y), (*cushion, 255))

    return add_outline(img)


# ============================================================
# NEW COMMON ITEMS (16)
# ============================================================

def make_newspaper():
    """Newspaper (신문지)."""
    img = new_sprite(32)
    paper = (240, 235, 220)
    paper_dark = (210, 205, 190)
    text = (80, 80, 80)
    headline = (40, 40, 40)

    # Paper sheets (slightly askew)
    fill_rect(img, 5, 8, 27, 28, paper)
    fill_rect(img, 4, 9, 6, 27, paper_dark)

    # Fold line
    fill_rect(img, 5, 17, 27, 18, paper_dark)

    # Headline
    fill_rect(img, 8, 10, 24, 12, headline)

    # Text lines
    for y in range(14, 17):
        fill_rect(img, 8, y, 22, y, text)
    for y in range(20, 27, 2):
        fill_rect(img, 8, y, 24, y, text)
        fill_rect(img, 8, y + 1, 18, y + 1, text)

    # Corner fold
    pixels = {}
    for i in range(5):
        for j in range(5 - i):
            pixels[(27 - j, 8 + i)] = paper_dark
    put_pixels(img, pixels)

    return add_outline(img)


def make_paper_bag():
    """Paper bag (종이봉투)."""
    img = new_sprite(32)
    bag = (180, 150, 100)
    bag_dark = (150, 120, 75)
    bag_light = (200, 175, 130)
    fold = (140, 110, 70)

    # Bag body
    fill_rect(img, 7, 10, 25, 29, bag)
    fill_rect(img, 7, 10, 15, 29, bag_dark)

    # Top opening (folded)
    fill_rect(img, 6, 8, 26, 11, bag_light)
    fill_rect(img, 8, 6, 24, 9, bag)

    # Fold creases
    fill_rect(img, 16, 10, 16, 29, fold)

    # Bottom fold
    fill_rect(img, 7, 27, 25, 28, fold)

    # Handle holes
    fill_rect(img, 12, 7, 14, 8, fold)
    fill_rect(img, 18, 7, 20, 8, fold)

    return add_outline(img)


def make_blanket():
    """Blanket (담요)."""
    img = new_sprite(32)
    fabric = (180, 200, 230)
    fabric_dark = (150, 170, 200)
    fabric_light = (210, 225, 245)
    edge = (140, 160, 190)

    # Folded blanket shape
    fill_rect(img, 4, 16, 28, 28, fabric)
    fill_rect(img, 5, 12, 27, 17, fabric_light)
    fill_rect(img, 6, 10, 26, 13, fabric)

    # Folds/wrinkles
    fill_rect(img, 10, 18, 10, 26, fabric_dark)
    fill_rect(img, 18, 18, 18, 26, fabric_dark)

    # Edge trim
    fill_rect(img, 4, 28, 28, 29, edge)
    fill_rect(img, 5, 11, 7, 11, edge)

    # Plaid pattern
    for x in range(6, 27, 4):
        fill_rect(img, x, 16, x, 27, fabric_dark)
    for y in range(18, 28, 4):
        fill_rect(img, 4, y, 28, y, fabric_dark)

    return add_outline(img)


def make_water_bowl():
    """Water bowl (물그릇)."""
    img = new_sprite(32)
    bowl = (100, 140, 200)
    bowl_dark = (70, 110, 170)
    bowl_light = (140, 180, 230)
    water = (150, 200, 240)
    water_light = (200, 230, 255)

    cx, cy = 16, 20
    for y in range(17, 29):
        for x in range(32):
            dx = (x - cx) / 11
            dy = (y - cy) / 8
            if dx * dx + dy * dy <= 1:
                if x < 13:
                    img.putpixel((x, y), (*bowl_dark, 255))
                elif x > 19:
                    img.putpixel((x, y), (*bowl_light, 255))
                else:
                    img.putpixel((x, y), (*bowl, 255))

    # Inner rim
    for x in range(8, 25):
        img.putpixel((x, 17), (220, 220, 230, 255))
        img.putpixel((x, 18), (220, 220, 230, 255))

    # Water inside
    for y in range(17, 21):
        for x in range(9, 24):
            dx = (x - cx) / 10
            dy = (y - 18) / 3
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*water, 255))

    # Water shine
    fill_rect(img, 11, 18, 14, 18, water_light)

    # Paw print on bowl
    img.putpixel((16, 23), (*bowl_light, 255))
    img.putpixel((15, 22), (*bowl_light, 255))
    img.putpixel((17, 22), (*bowl_light, 255))

    return add_outline(img)


def make_slipper():
    """Slipper (슬리퍼)."""
    img = new_sprite(32)
    fabric = (255, 180, 200)
    fabric_dark = (230, 150, 170)
    sole = (200, 180, 160)
    sole_dark = (170, 150, 130)
    inner = (255, 210, 220)

    # Sole
    for y in range(22, 30):
        for x in range(32):
            dx = (x - 15) / 11
            dy = (y - 26) / 4
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*sole, 255))

    # Shoe body
    for y in range(16, 26):
        for x in range(32):
            dx = (x - 14) / 10
            dy = (y - 21) / 5
            if dx * dx + dy * dy <= 1 and y < 25:
                img.putpixel((x, y), (*fabric, 255))

    # Inner opening
    for y in range(17, 22):
        for x in range(17, 25):
            dx = (x - 20) / 5
            dy = (y - 19) / 3
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*inner, 255))

    # Toe bump
    fill_rect(img, 4, 20, 8, 24, fabric_dark)

    return add_outline(img)


def make_tissue_box():
    """Tissue box (티슈박스)."""
    img = new_sprite(32)
    box = (180, 220, 240)
    box_dark = (150, 190, 210)
    box_light = (210, 240, 250)
    tissue = (255, 255, 255)
    tissue_shadow = (230, 230, 235)
    opening = (100, 100, 110)

    # Box body (3D)
    fill_rect(img, 5, 14, 27, 28, box)
    fill_rect(img, 5, 14, 15, 28, box_dark)
    fill_rect(img, 5, 12, 27, 15, box_light)

    # Opening slit
    fill_rect(img, 12, 12, 20, 13, opening)

    # Tissue sticking out
    fill_rect(img, 13, 6, 19, 13, tissue)
    fill_rect(img, 12, 5, 20, 7, tissue)
    fill_rect(img, 14, 7, 14, 12, tissue_shadow)
    fill_rect(img, 18, 8, 18, 12, tissue_shadow)

    # Decorative stripe
    fill_rect(img, 5, 20, 27, 22, box_dark)

    return add_outline(img)


def make_sock():
    """Sock (양말)."""
    img = new_sprite(32)
    sock = (240, 200, 100)
    sock_dark = (210, 170, 70)
    stripe1 = (230, 100, 80)
    stripe2 = (100, 180, 120)
    toe = (240, 220, 150)

    # Leg part (vertical)
    fill_rect(img, 12, 4, 20, 18, sock)

    # Cuff
    fill_rect(img, 11, 4, 21, 7, sock_dark)
    fill_rect(img, 11, 5, 21, 5, stripe1)

    # Stripes
    fill_rect(img, 12, 10, 20, 11, stripe1)
    fill_rect(img, 12, 14, 20, 15, stripe2)

    # Heel turn
    fill_rect(img, 8, 18, 20, 24, sock)
    fill_rect(img, 6, 20, 18, 26, sock)

    # Toe
    for y in range(22, 28):
        for x in range(4, 16):
            dx = (x - 10) / 6
            dy = (y - 25) / 3
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*toe, 255))

    return add_outline(img)


def make_shoe_box():
    """Shoe box (신발상자)."""
    img = new_sprite(32)
    box = (200, 100, 80)
    box_dark = (170, 75, 55)
    box_light = (225, 130, 110)
    lid = (220, 120, 100)
    label = (255, 255, 240)

    # Box body
    fill_rect(img, 4, 14, 28, 28, box)
    fill_rect(img, 4, 14, 15, 28, box_dark)

    # Lid (slightly ajar)
    fill_rect(img, 3, 10, 29, 14, lid)
    fill_rect(img, 4, 9, 28, 11, box_light)

    # Label on front
    fill_rect(img, 12, 18, 22, 24, label)

    # Label text (tiny lines)
    fill_rect(img, 14, 19, 20, 19, box_dark)
    fill_rect(img, 14, 21, 18, 21, box_dark)
    fill_rect(img, 14, 23, 20, 23, box_dark)

    return add_outline(img)


def make_milk_carton():
    """Milk carton (우유팩)."""
    img = new_sprite(32)
    carton = (245, 245, 250)
    blue = (100, 150, 220)
    blue_dark = (70, 120, 190)
    red = (220, 80, 80)
    top = (230, 230, 235)

    # Carton body
    fill_rect(img, 8, 10, 24, 29, carton)
    fill_rect(img, 8, 10, 15, 29, (235, 235, 240))

    # Blue stripe (milk brand)
    fill_rect(img, 8, 14, 24, 20, blue)
    fill_rect(img, 8, 14, 15, 20, blue_dark)

    # Top triangular fold
    fill_rect(img, 10, 7, 22, 10, top)
    fill_rect(img, 12, 5, 20, 8, carton)
    fill_rect(img, 14, 4, 18, 6, top)
    fill_rect(img, 15, 3, 17, 5, carton)

    # "MILK" text area
    fill_rect(img, 12, 16, 20, 18, (255, 255, 255))

    # Red cap
    fill_rect(img, 18, 6, 22, 9, red)

    return add_outline(img)


def make_tin_can():
    """Tin can (깡통)."""
    img = new_sprite(32)
    metal = (180, 185, 190)
    metal_dark = (140, 145, 150)
    metal_light = (210, 215, 220)
    label = (200, 80, 60)
    label_dark = (170, 60, 45)
    rim = (160, 165, 170)

    # Can body (cylinder)
    fill_rect(img, 8, 8, 24, 28, metal)
    fill_rect(img, 8, 8, 15, 28, metal_dark)
    fill_rect(img, 20, 8, 24, 28, metal_light)

    # Top rim
    fill_rect(img, 7, 7, 25, 9, rim)

    # Bottom rim
    fill_rect(img, 7, 27, 25, 29, rim)

    # Label
    fill_rect(img, 8, 14, 24, 24, label)
    fill_rect(img, 8, 14, 15, 24, label_dark)

    # Label fish icon
    fill_rect(img, 13, 17, 19, 21, (255, 200, 100))

    return add_outline(img)


def make_leaf():
    """Leaf (나뭇잎)."""
    img = new_sprite(32)
    green = (80, 180, 80)
    green_dark = (50, 140, 50)
    green_light = (120, 210, 110)
    stem = (100, 80, 40)
    vein = (60, 150, 60)

    # Leaf shape (pointed oval)
    cx, cy = 16, 15
    for y in range(32):
        for x in range(32):
            dx = (x - cx) / 9
            dy = (y - cy) / 10
            dist = dx * dx + dy * dy
            if dist <= 1 and y < 28:
                # Make pointed at top
                if y < 8 and abs(x - cx) > (y - 4):
                    continue
                if y < cy:
                    img.putpixel((x, y), (*green_light, 255))
                else:
                    img.putpixel((x, y), (*green, 255))

    # Center vein
    for y in range(6, 26):
        if 0 <= y < 32:
            img.putpixel((16, y), (*vein, 255))

    # Side veins
    for i in range(3):
        y_base = 12 + i * 4
        for dx in range(1, 5):
            if 0 <= 16 - dx < 32 and 0 <= y_base + dx < 32:
                img.putpixel((16 - dx, y_base + dx), (*vein, 255))
            if 0 <= 16 + dx < 32 and 0 <= y_base + dx < 32:
                img.putpixel((16 + dx, y_base + dx), (*vein, 255))

    # Stem
    for y in range(25, 31):
        img.putpixel((16, y), (*stem, 255))

    return add_outline(img)


def make_pine_cone():
    """Pine cone (솔방울)."""
    img = new_sprite(32)
    brown = (140, 90, 40)
    brown_dark = (110, 65, 25)
    brown_light = (175, 125, 70)
    stem_color = (100, 70, 30)

    # Oval body
    cx, cy = 16, 17
    for y in range(32):
        for x in range(32):
            dx = (x - cx) / 7
            dy = (y - cy) / 9
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*brown, 255))

    # Scale pattern (overlapping V shapes)
    for row in range(0, 16, 3):
        y = 10 + row
        offset = 2 if (row // 3) % 2 else 0
        for col in range(-2, 4):
            x = 10 + col * 4 + offset
            if 0 <= x < 32 and 0 <= y < 32:
                px = img.getpixel((x, y))
                if px[3] > 0:
                    img.putpixel((x, y), (*brown_dark, 255))
                    if x + 1 < 32 and img.getpixel((x + 1, y))[3] > 0:
                        img.putpixel((x + 1, y), (*brown_light, 255))

    # Stem
    fill_rect(img, 15, 7, 17, 10, stem_color)

    return add_outline(img)


def make_rubber_duck():
    """Rubber duck (고무 오리)."""
    img = new_sprite(32)
    yellow = (255, 220, 50)
    yellow_dark = (230, 190, 30)
    yellow_light = (255, 240, 120)
    beak = (255, 150, 30)
    eye = (20, 20, 20)
    eye_white = (255, 255, 255)

    # Body (round)
    cx, cy = 16, 20
    for y in range(32):
        for x in range(32):
            dx = (x - cx) / 10
            dy = (y - cy) / 8
            if dx * dx + dy * dy <= 1:
                if x < 12:
                    img.putpixel((x, y), (*yellow_dark, 255))
                else:
                    img.putpixel((x, y), (*yellow, 255))

    # Head (smaller circle on top)
    hx, hy = 18, 11
    for y in range(32):
        for x in range(32):
            dx = (x - hx) / 6
            dy = (y - hy) / 6
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*yellow, 255))

    # Beak
    fill_rect(img, 23, 10, 27, 13, beak)

    # Eye
    img.putpixel((20, 9), (*eye_white, 255))
    img.putpixel((21, 9), (*eye_white, 255))
    img.putpixel((21, 9), (*eye, 255))

    # Highlight
    img.putpixel((14, 8), (*yellow_light, 255))
    img.putpixel((15, 7), (*yellow_light, 255))

    return add_outline(img)


def make_ball():
    """Ball (공)."""
    img = new_sprite(32)
    red = (220, 60, 60)
    blue = (60, 100, 220)
    white = (240, 240, 245)
    highlight = (255, 255, 255)

    cx, cy, r = 16, 16, 9
    for y in range(32):
        for x in range(32):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if dist <= r:
                # Split into sections
                angle = __import__('math').atan2(y - cy, x - cx)
                if angle < -1.0:
                    img.putpixel((x, y), (*red, 255))
                elif angle < 0.5:
                    img.putpixel((x, y), (*white, 255))
                elif angle < 2.0:
                    img.putpixel((x, y), (*blue, 255))
                else:
                    img.putpixel((x, y), (*red, 255))

    # Dividing lines
    for t in range(60):
        a = t * 0.105
        x = int(cx + r * __import__('math').cos(a))
        y = int(cy + r * __import__('math').sin(a))
        if 0 <= x < 32 and 0 <= y < 32:
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if dist <= r:
                img.putpixel((x, y), (40, 40, 40, 255))

    # Highlight
    img.putpixel((12, 10), (*highlight, 255))
    img.putpixel((13, 11), (*highlight, 255))

    return add_outline(img)


def make_pencil():
    """Pencil (연필)."""
    img = new_sprite(32)
    yellow = (255, 210, 50)
    yellow_dark = (230, 185, 30)
    wood = (210, 170, 120)
    graphite = (60, 60, 60)
    eraser = (255, 130, 140)
    metal = (180, 185, 190)

    # Pencil body (diagonal)
    for i in range(20):
        x = 4 + i
        y = 24 - i
        for dy in range(-1, 2):
            if 0 <= y + dy < 32:
                img.putpixel((x, y + dy), (*yellow, 255))
                if dy == -1:
                    img.putpixel((x, y + dy), (*yellow_dark, 255))

    # Tip (wood + graphite)
    for i in range(3):
        x = 4 - i + i
        y = 24 + i
        img.putpixel((3 - i, 25 + i), (*wood, 255))
    img.putpixel((2, 26), (*wood, 255))
    img.putpixel((3, 25), (*wood, 255))
    img.putpixel((1, 27), (*graphite, 255))

    # Eraser end
    for i in range(3):
        x = 24 + i
        y = 4 - i
        for dy in range(-1, 2):
            if 0 <= y + dy < 32 and 0 <= x < 32:
                img.putpixel((x, y + dy), (*eraser, 255))

    # Metal ferrule
    img.putpixel((23, 5), (*metal, 255))
    img.putpixel((23, 6), (*metal, 255))
    img.putpixel((24, 4), (*metal, 255))
    img.putpixel((24, 5), (*metal, 255))

    return add_outline(img)


def make_plastic_cup():
    """Plastic cup (플라스틱 컵)."""
    img = new_sprite(32)
    cup = (230, 240, 250)
    cup_dark = (200, 210, 220)
    cup_light = (245, 250, 255)
    rim = (210, 220, 230)
    straw = (255, 100, 100)

    # Cup body (trapezoid)
    for row in range(18):
        y = 28 - row
        half_w = int(5 + row * 0.2)
        x0 = 16 - half_w
        x1 = 16 + half_w
        fill_rect(img, x0, y, x1, y, cup)

    # Left shadow
    for row in range(18):
        y = 28 - row
        half_w = int(5 + row * 0.2)
        x0 = 16 - half_w
        if 0 <= x0 + 1 < 32:
            img.putpixel((x0, y), (*cup_dark, 255))
            img.putpixel((x0 + 1, y), (*cup_dark, 255))

    # Rim
    fill_rect(img, 9, 10, 23, 12, rim)

    # Straw
    for y in range(2, 22):
        img.putpixel((20, y), (*straw, 255))
        if y < 5:
            img.putpixel((21, y), (*straw, 255))

    # Highlight reflection
    fill_rect(img, 18, 14, 18, 24, cup_light)

    return add_outline(img)


# ============================================================
# NEW RARE ITEMS (16)
# ============================================================

def make_laser_pointer():
    """Laser pointer (레이저 포인터)."""
    img = new_sprite(32)
    body = (60, 60, 65)
    body_light = (90, 90, 95)
    button = (200, 50, 50)
    beam = (255, 30, 30)
    lens = (180, 30, 30)

    # Pointer body (horizontal cylinder)
    fill_rect(img, 4, 14, 24, 18, body)
    fill_rect(img, 4, 15, 24, 17, body_light)

    # Rounded ends
    fill_rect(img, 3, 15, 4, 17, body)
    fill_rect(img, 24, 15, 25, 17, body)

    # Button
    fill_rect(img, 12, 13, 15, 14, button)

    # Clip
    fill_rect(img, 6, 12, 10, 14, body_light)

    # Lens
    fill_rect(img, 25, 15, 26, 17, lens)

    # Beam
    for x in range(27, 32):
        img.putpixel((x, 16), (*beam, 255))

    # Red dot (target)
    img.putpixel((30, 15), (*beam, 200))
    img.putpixel((30, 17), (*beam, 200))

    # Key ring
    img.putpixel((3, 16), (160, 160, 165, 255))
    img.putpixel((2, 15), (160, 160, 165, 255))
    img.putpixel((2, 17), (160, 160, 165, 255))
    img.putpixel((1, 16), (160, 160, 165, 255))

    return add_outline(img)


def make_bell_toy():
    """Bell toy (방울 장난감)."""
    img = new_sprite(32)
    gold = (255, 200, 50)
    gold_dark = (200, 160, 30)
    gold_light = (255, 230, 120)
    slit = (40, 40, 40)
    ring = (180, 140, 20)

    # Bell body (sphere)
    cx, cy, r = 16, 18, 8
    for y in range(32):
        for x in range(32):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if dist <= r:
                if x < cx - 2:
                    img.putpixel((x, y), (*gold_dark, 255))
                elif x > cx + 2:
                    img.putpixel((x, y), (*gold_light, 255))
                else:
                    img.putpixel((x, y), (*gold, 255))

    # Bottom slit
    fill_rect(img, 12, 25, 20, 25, slit)
    img.putpixel((16, 26), (*slit, 255))

    # Top loop
    fill_rect(img, 14, 8, 18, 10, ring)
    fill_rect(img, 15, 7, 17, 8, ring)
    img.putpixel((15, 9), (0, 0, 0, 0))
    img.putpixel((16, 9), (0, 0, 0, 0))
    img.putpixel((17, 9), (0, 0, 0, 0))

    # Highlight
    img.putpixel((12, 14), (*gold_light, 255))
    img.putpixel((13, 13), (255, 255, 200, 255))

    return add_outline(img)


def make_catnip():
    """Catnip (캣닢)."""
    img = new_sprite(32)
    bag = (200, 180, 140)
    bag_dark = (170, 150, 110)
    green = (80, 170, 80)
    green_dark = (50, 130, 50)
    green_light = (120, 200, 110)
    tie = (180, 80, 80)

    # Small bag
    fill_rect(img, 8, 12, 24, 26, bag)
    fill_rect(img, 8, 12, 15, 26, bag_dark)

    # Bag top (gathered)
    fill_rect(img, 10, 10, 22, 13, bag)
    fill_rect(img, 12, 8, 20, 11, bag)

    # Tie
    fill_rect(img, 13, 10, 19, 11, tie)

    # Leaves spilling out top
    pixels = {}
    for pos in [(14, 6), (15, 5), (16, 4), (17, 5), (18, 6),
                (12, 7), (13, 6), (19, 6), (20, 7)]:
        pixels[pos] = green
    for pos in [(15, 4), (16, 3), (17, 4)]:
        pixels[pos] = green_light
    put_pixels(img, pixels)

    # Label (paw print)
    img.putpixel((16, 18), (*green_dark, 255))
    img.putpixel((15, 17), (*green_dark, 255))
    img.putpixel((17, 17), (*green_dark, 255))
    img.putpixel((14, 19), (*green_dark, 255))
    img.putpixel((18, 19), (*green_dark, 255))

    # Star sparkles (it's special!)
    img.putpixel((6, 8), (255, 255, 150, 255))
    img.putpixel((25, 6), (255, 255, 150, 255))

    return add_outline(img)


def make_tunnel():
    """Tunnel (터널)."""
    img = new_sprite(32)
    fabric = (140, 100, 180)
    fabric_dark = (110, 70, 150)
    fabric_light = (170, 140, 210)
    inside = (40, 20, 60)
    wire = (180, 160, 200)

    # Tube body (horizontal cylinder)
    fill_rect(img, 2, 10, 30, 26, fabric)
    fill_rect(img, 2, 10, 30, 16, fabric_light)
    fill_rect(img, 2, 22, 30, 26, fabric_dark)

    # Opening (left circle)
    cx, cy = 6, 18
    for y in range(32):
        for x in range(32):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if dist <= 8:
                if dist <= 6:
                    img.putpixel((x, y), (*inside, 255))
                else:
                    img.putpixel((x, y), (*fabric, 255))

    # Wire rings
    for ring_x in [14, 22]:
        fill_rect(img, ring_x, 10, ring_x + 1, 26, wire)

    # Crinkle texture
    for y in range(12, 24, 3):
        fill_rect(img, 8, y, 28, y, fabric_dark)

    return add_outline(img)


def make_hammock():
    """Hammock (해먹)."""
    img = new_sprite(32)
    fabric = (255, 180, 140)
    fabric_dark = (230, 150, 110)
    rope = (160, 140, 100)
    pole = (120, 100, 70)

    # Poles
    fill_rect(img, 4, 4, 6, 28, pole)
    fill_rect(img, 26, 4, 28, 28, pole)

    # Ropes
    for i in range(6):
        img.putpixel((7 + i, 6 + i), (*rope, 255))
        img.putpixel((25 - i, 6 + i), (*rope, 255))

    # Fabric (curved/sagging)
    for x in range(10, 23):
        dx = (x - 16) / 6
        sag = int(dx * dx * 4)
        y_top = 12 + sag
        for y in range(y_top, y_top + 5):
            if 0 <= y < 32:
                if y == y_top:
                    img.putpixel((x, y), (*fabric_dark, 255))
                else:
                    img.putpixel((x, y), (*fabric, 255))

    # Pole tops
    fill_rect(img, 3, 3, 7, 5, pole)
    fill_rect(img, 25, 3, 29, 5, pole)

    # Fringe at edges
    for dy in range(3):
        img.putpixel((10, 16 + dy), (*fabric_dark, 255))
        img.putpixel((22, 16 + dy), (*fabric_dark, 255))

    return add_outline(img)


def make_feather_wand():
    """Feather wand (깃털 낚시대)."""
    img = new_sprite(32)
    stick = (160, 120, 70)
    stick_dark = (130, 95, 50)
    string = (180, 180, 180)
    feather1 = (255, 100, 120)
    feather2 = (100, 180, 255)
    feather3 = (255, 200, 80)

    # Stick (diagonal)
    for i in range(20):
        x = 22 - i
        y = 28 - i
        if 0 <= x < 32 and 0 <= y < 32:
            img.putpixel((x, y), (*stick, 255))
            if y + 1 < 32:
                img.putpixel((x, y + 1), (*stick_dark, 255))

    # String from tip
    for i in range(6):
        img.putpixel((3 + i, 8 + i), (*string, 255))

    # Feathers at end
    for i in range(5):
        img.putpixel((8 + i, 14 - i), (*feather1, 255))
        img.putpixel((9 + i, 14 - i), (*feather1, 255))
    for i in range(5):
        img.putpixel((10 + i, 13 - i), (*feather2, 255))
        img.putpixel((11 + i, 13 - i), (*feather2, 255))
    for i in range(4):
        img.putpixel((7 + i, 15 - i), (*feather3, 255))
        img.putpixel((8 + i, 15 - i), (*feather3, 255))

    # Handle wrap
    for i in range(3):
        x = 20 + i
        y = 26 + i
        if 0 <= x < 32 and 0 <= y < 32:
            img.putpixel((x, y), (200, 80, 80, 255))

    return add_outline(img)


def make_mirror():
    """Mirror (거울)."""
    img = new_sprite(32)
    frame = (180, 140, 60)
    frame_dark = (150, 110, 40)
    glass = (200, 220, 240)
    glass_light = (240, 245, 255)
    handle = (160, 120, 50)

    # Mirror frame (oval)
    cx, cy = 16, 13
    for y in range(32):
        for x in range(32):
            dx = (x - cx) / 9
            dy = (y - cy) / 9
            dist = dx * dx + dy * dy
            if dist <= 1:
                if dist > 0.7:
                    img.putpixel((x, y), (*frame, 255))
                else:
                    img.putpixel((x, y), (*glass, 255))

    # Glass shine
    fill_rect(img, 12, 8, 14, 11, glass_light)
    img.putpixel((11, 9), (*glass_light, 255))

    # Handle
    fill_rect(img, 15, 22, 17, 29, handle)
    fill_rect(img, 14, 28, 18, 30, frame_dark)

    # Decorative top
    img.putpixel((16, 3), (*frame, 255))
    img.putpixel((15, 4), (*frame, 255))
    img.putpixel((17, 4), (*frame, 255))

    return add_outline(img)


def make_music_box():
    """Music box (오르골)."""
    img = new_sprite(32)
    wood = (160, 110, 60)
    wood_dark = (130, 85, 40)
    wood_light = (190, 140, 85)
    metal = (200, 190, 150)
    gold = (220, 190, 80)
    note = (60, 60, 60)

    # Box body
    fill_rect(img, 5, 14, 27, 28, wood)
    fill_rect(img, 5, 14, 15, 28, wood_dark)

    # Lid (open at angle)
    fill_rect(img, 5, 10, 27, 14, wood_light)
    fill_rect(img, 6, 7, 26, 11, wood)

    # Metal hinge
    fill_rect(img, 5, 12, 7, 14, metal)

    # Gold trim
    fill_rect(img, 6, 14, 26, 15, gold)

    # Interior detail
    fill_rect(img, 8, 16, 24, 18, wood_light)

    # Music notes floating
    pixels = {}
    for pos in [(20, 4), (22, 3), (24, 5)]:
        pixels[pos] = note
    # Note stems
    for pos in [(20, 5), (20, 6), (22, 4), (22, 5), (24, 6), (24, 7)]:
        pixels[pos] = note
    put_pixels(img, pixels)

    # Keyhole
    img.putpixel((16, 22), (*gold, 255))
    img.putpixel((16, 23), (*gold, 255))

    return add_outline(img)


def make_ribbon():
    """Ribbon (리본)."""
    img = new_sprite(32)
    pink = (255, 120, 160)
    pink_dark = (220, 80, 120)
    pink_light = (255, 170, 200)
    center = (200, 60, 100)

    # Left loop
    cx, cy = 10, 14
    for y in range(32):
        for x in range(32):
            dx = (x - cx) / 6
            dy = (y - cy) / 7
            dist = dx * dx + dy * dy
            if 0.3 < dist <= 1:
                img.putpixel((x, y), (*pink, 255))
            elif dist <= 0.3:
                img.putpixel((x, y), (*pink_light, 255))

    # Right loop
    cx2, cy2 = 22, 14
    for y in range(32):
        for x in range(32):
            dx = (x - cx2) / 6
            dy = (y - cy2) / 7
            dist = dx * dx + dy * dy
            if 0.3 < dist <= 1:
                px = img.getpixel((x, y))
                if px[3] == 0:
                    img.putpixel((x, y), (*pink, 255))
            elif dist <= 0.3:
                img.putpixel((x, y), (*pink_light, 255))

    # Center knot
    fill_rect(img, 14, 12, 18, 18, center)

    # Tails
    for i in range(6):
        img.putpixel((14 - i, 19 + i), (*pink_dark, 255))
        img.putpixel((13 - i, 19 + i), (*pink, 255))
        img.putpixel((18 + i, 19 + i), (*pink_dark, 255))
        img.putpixel((19 + i, 19 + i), (*pink, 255))

    return add_outline(img)


def make_brush():
    """Brush (빗)."""
    img = new_sprite(32)
    handle = (160, 120, 70)
    handle_dark = (130, 95, 50)
    bristle = (220, 210, 200)
    bristle_dark = (190, 180, 170)
    pad = (140, 100, 60)

    # Handle
    fill_rect(img, 13, 4, 19, 14, handle)
    fill_rect(img, 14, 4, 18, 14, handle_dark)

    # Brush head (pad)
    fill_rect(img, 8, 14, 24, 18, pad)

    # Bristles
    for x in range(9, 24, 2):
        fill_rect(img, x, 18, x, 28, bristle)
        fill_rect(img, x, 27, x, 29, bristle_dark)

    # Handle top
    fill_rect(img, 14, 3, 18, 5, handle)

    # Hole in handle
    img.putpixel((16, 6), (0, 0, 0, 0))
    img.putpixel((16, 7), (0, 0, 0, 0))

    return add_outline(img)


def make_treat_jar():
    """Treat jar (간식통)."""
    img = new_sprite(32)
    glass = (220, 230, 240)
    glass_dark = (190, 200, 210)
    glass_light = (240, 245, 255)
    lid = (200, 80, 80)
    lid_dark = (170, 60, 60)
    treat = (200, 160, 80)

    # Jar body
    fill_rect(img, 8, 10, 24, 27, glass)
    fill_rect(img, 8, 10, 14, 27, glass_dark)
    fill_rect(img, 20, 10, 24, 27, glass_light)

    # Base
    fill_rect(img, 7, 27, 25, 29, glass_dark)

    # Lid
    fill_rect(img, 7, 8, 25, 11, lid)
    fill_rect(img, 9, 6, 23, 9, lid)
    fill_rect(img, 12, 4, 20, 7, lid_dark)

    # Knob
    fill_rect(img, 14, 3, 18, 5, lid)

    # Treats inside (fish shapes)
    for pos in [(12, 18), (16, 22), (20, 16), (14, 24), (18, 20)]:
        img.putpixel(pos, (*treat, 255))
        if pos[0] + 1 < 24:
            img.putpixel((pos[0] + 1, pos[1]), (*treat, 255))

    # Shine
    fill_rect(img, 21, 12, 22, 20, glass_light)

    return add_outline(img)


def make_pillow():
    """Pillow (베개)."""
    img = new_sprite(32)
    fabric = (200, 180, 230)
    fabric_dark = (170, 150, 200)
    fabric_light = (225, 210, 245)

    # Pillow shape (rounded rectangle)
    cx, cy = 16, 17
    for y in range(32):
        for x in range(32):
            dx = (x - cx) / 12
            dy = (y - cy) / 7
            dist = dx * dx + dy * dy
            if dist <= 1:
                if dist > 0.7:
                    img.putpixel((x, y), (*fabric_dark, 255))
                elif y < cy - 2:
                    img.putpixel((x, y), (*fabric_light, 255))
                else:
                    img.putpixel((x, y), (*fabric, 255))

    # Corner puffs
    for cx2, cy2 in [(6, 12), (26, 12), (6, 22), (26, 22)]:
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                nx, ny = cx2 + dx, cy2 + dy
                if 0 <= nx < 32 and 0 <= ny < 32:
                    img.putpixel((nx, ny), (*fabric_dark, 255))

    # Stitch line
    for x in range(8, 25, 3):
        img.putpixel((x, 17), (*fabric_dark, 255))

    return add_outline(img)


def make_rug():
    """Rug (러그)."""
    img = new_sprite(32)
    main_color = (180, 80, 80)
    border = (120, 50, 50)
    pattern = (220, 180, 100)
    fringe = (200, 160, 80)

    # Rug body (flat rectangle with perspective)
    fill_rect(img, 3, 14, 29, 26, main_color)

    # Border
    draw_outline(img, 3, 14, 29, 26, border)
    draw_outline(img, 5, 16, 27, 24, border)

    # Center pattern (diamond)
    cx, cy = 16, 20
    for d in range(4):
        img.putpixel((cx, cy - d), (*pattern, 255))
        img.putpixel((cx, cy + d), (*pattern, 255))
        img.putpixel((cx - d, cy), (*pattern, 255))
        img.putpixel((cx + d, cy), (*pattern, 255))

    # Corner patterns
    for x, y in [(8, 18), (24, 18), (8, 22), (24, 22)]:
        img.putpixel((x, y), (*pattern, 255))
        img.putpixel((x + 1, y), (*pattern, 255))

    # Fringe top and bottom
    for x in range(4, 29, 2):
        img.putpixel((x, 13), (*fringe, 255))
        img.putpixel((x, 12), (*fringe, 255))
        img.putpixel((x, 27), (*fringe, 255))
        img.putpixel((x, 28), (*fringe, 255))

    return add_outline(img)


def make_basket():
    """Basket (바구니)."""
    img = new_sprite(32)
    wicker = (190, 150, 90)
    wicker_dark = (160, 120, 65)
    wicker_light = (215, 180, 120)
    inside = (100, 70, 40)

    # Basket body (bowl shape)
    for row in range(14):
        y = 28 - row
        half_w = int(6 + row * 0.4)
        x0 = 16 - half_w
        x1 = 16 + half_w
        if (row // 2) % 2 == 0:
            fill_rect(img, x0, y, x1, y, wicker)
        else:
            fill_rect(img, x0, y, x1, y, wicker_dark)

    # Weave pattern
    for y in range(16, 28, 2):
        for x in range(6, 27, 3):
            px = img.getpixel((x, y))
            if px[3] > 0:
                img.putpixel((x, y), (*wicker_light, 255))

    # Rim
    fill_rect(img, 5, 14, 27, 16, wicker_light)
    fill_rect(img, 5, 14, 27, 14, wicker_dark)

    # Inside shadow
    fill_rect(img, 8, 15, 24, 17, inside)

    # Handle
    for i in range(8):
        x = 12 + i
        y = int(12 - 3 * (1 - ((i - 4) / 4) ** 2))
        if 0 <= y < 32:
            img.putpixel((x, y), (*wicker_dark, 255))
            img.putpixel((x, y + 1), (*wicker, 255))

    return add_outline(img)


def make_lantern():
    """Lantern (랜턴)."""
    img = new_sprite(32)
    metal = (80, 80, 85)
    metal_light = (120, 120, 125)
    glass = (255, 220, 120)
    glass_light = (255, 240, 180)
    flame = (255, 160, 50)
    flame_top = (255, 100, 30)

    # Handle
    fill_rect(img, 14, 3, 18, 5, metal)
    fill_rect(img, 13, 5, 19, 6, metal)
    img.putpixel((15, 2), (*metal, 255))
    img.putpixel((17, 2), (*metal, 255))
    img.putpixel((16, 1), (*metal, 255))

    # Top cap
    fill_rect(img, 10, 6, 22, 8, metal)

    # Glass body (glowing)
    fill_rect(img, 10, 8, 22, 22, glass)
    fill_rect(img, 11, 8, 15, 22, glass_light)

    # Metal frame
    fill_rect(img, 10, 8, 10, 22, metal)
    fill_rect(img, 22, 8, 22, 22, metal)
    fill_rect(img, 16, 8, 16, 22, metal)

    # Flame
    fill_rect(img, 15, 12, 17, 18, flame)
    img.putpixel((16, 11), (*flame_top, 255))
    img.putpixel((16, 10), (*flame_top, 200))

    # Base
    fill_rect(img, 10, 22, 22, 24, metal)
    fill_rect(img, 11, 24, 21, 26, metal_light)

    # Glow effect
    for pos in [(9, 12), (23, 14), (9, 18), (23, 18)]:
        img.putpixel(pos, (255, 220, 120, 100))

    return add_outline(img)


def make_wind_chime():
    """Wind chime (풍경)."""
    img = new_sprite(32)
    metal = (180, 200, 220)
    metal_dark = (140, 160, 180)
    string = (160, 160, 160)
    ring = (200, 180, 100)
    pendant = (180, 80, 80)

    # Top ring
    fill_rect(img, 12, 2, 20, 4, ring)
    fill_rect(img, 13, 1, 19, 2, ring)
    fill_rect(img, 14, 3, 18, 3, (0, 0, 0, 0))

    # Strings
    for x_pos in [10, 14, 18, 22]:
        for y in range(4, 10):
            img.putpixel((x_pos, y), (*string, 255))

    # Chime tubes (different lengths)
    lengths = [12, 16, 18, 14]
    for i, (x_pos, length) in enumerate(zip([10, 14, 18, 22], lengths)):
        for y in range(10, 10 + length):
            if 0 <= y < 32:
                img.putpixel((x_pos, y), (*metal, 255))
                img.putpixel((x_pos - 1, y), (*metal_dark, 255))

    # Center pendant (wind catcher)
    img.putpixel((16, 10), (*string, 255))
    for y in range(11, 16):
        img.putpixel((16, y), (*string, 255))
    # Paper pendant
    fill_rect(img, 14, 16, 18, 22, pendant)
    fill_rect(img, 15, 22, 17, 24, pendant)

    return add_outline(img)


# ============================================================
# NEW EPIC ITEMS (16)
# ============================================================

def make_fountain():
    """Fountain (분수대)."""
    img = new_sprite(32)
    stone = (180, 175, 170)
    stone_dark = (150, 145, 140)
    water = (140, 200, 240)
    water_light = (200, 230, 255)
    splash = (220, 240, 255)

    # Base
    fill_rect(img, 4, 26, 28, 30, stone)
    fill_rect(img, 6, 24, 26, 27, stone)

    # Bowl
    for y in range(20, 26):
        for x in range(8, 24):
            dx = (x - 16) / 8
            dy = (y - 23) / 3
            if dx * dx + dy * dy <= 1:
                img.putpixel((x, y), (*stone_dark, 255))

    # Water in bowl
    fill_rect(img, 9, 21, 23, 23, water)

    # Center pillar
    fill_rect(img, 14, 10, 18, 22, stone)

    # Water jets (spraying up)
    for y in range(4, 12):
        img.putpixel((16, y), (*water_light, 255))
    # Splash at top
    for dx in [-3, -2, -1, 1, 2, 3]:
        img.putpixel((16 + dx, 5 + abs(dx)), (*splash, 255))

    # Falling water
    for dx in [-4, -3, 3, 4]:
        for dy in range(4):
            y = 8 + dy + abs(dx)
            if 0 <= 16 + dx < 32 and 0 <= y < 32:
                img.putpixel((16 + dx, y), (*water, 200))

    return add_outline(img)


def make_tree_house():
    """Tree house (나무집)."""
    img = new_sprite(32)
    trunk = (120, 85, 40)
    trunk_dark = (90, 60, 25)
    wood = (180, 140, 80)
    wood_dark = (150, 110, 55)
    roof = (160, 60, 40)
    leaf_color = (60, 150, 60)
    window = (200, 220, 240)

    # Trunk
    fill_rect(img, 13, 16, 19, 30, trunk)
    fill_rect(img, 14, 16, 17, 30, trunk_dark)

    # House body
    fill_rect(img, 5, 10, 27, 20, wood)
    fill_rect(img, 5, 10, 15, 20, wood_dark)

    # Roof (triangle)
    for row in range(6):
        y = 10 - row
        half_w = 12 - row * 2
        if half_w > 0:
            fill_rect(img, 16 - half_w, y, 16 + half_w, y, roof)

    # Window
    fill_rect(img, 13, 12, 19, 16, window)
    fill_rect(img, 16, 12, 16, 16, wood_dark)

    # Door
    fill_rect(img, 10, 15, 13, 20, trunk)

    # Leaves around
    for pos in [(3, 8), (4, 6), (6, 5), (26, 7), (28, 8), (27, 6),
                (8, 3), (10, 2), (20, 2), (22, 3), (24, 5)]:
        img.putpixel(pos, (*leaf_color, 255))
        if pos[0] + 1 < 32:
            img.putpixel((pos[0] + 1, pos[1]), (*leaf_color, 255))

    # Ladder
    fill_rect(img, 20, 20, 20, 28, trunk)
    fill_rect(img, 23, 20, 23, 28, trunk)
    for y in range(21, 28, 2):
        fill_rect(img, 20, y, 23, y, wood)

    return add_outline(img)


def make_hot_spring():
    """Hot spring (온천)."""
    img = new_sprite(32)
    rock = (130, 120, 110)
    rock_dark = (100, 90, 80)
    water = (140, 200, 230)
    water_light = (180, 220, 240)
    steam = (240, 240, 250)

    # Rock border
    for y in range(16, 30):
        for x in range(32):
            dx = (x - 16) / 13
            dy = (y - 22) / 7
            dist = dx * dx + dy * dy
            if dist <= 1:
                if dist > 0.6:
                    img.putpixel((x, y), (*rock, 255))
                else:
                    img.putpixel((x, y), (*water, 255))

    # Rock bumps
    for pos in [(5, 18), (10, 16), (16, 15), (22, 16), (27, 18)]:
        for dy in range(-2, 1):
            for dx in range(-2, 2):
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < 32 and 0 <= ny < 32:
                    img.putpixel((nx, ny), (*rock_dark, 255))

    # Water surface
    for x in range(8, 25):
        img.putpixel((x, 18), (*water_light, 255))

    # Steam wisps
    steam_positions = [(10, 12), (16, 10), (22, 12)]
    for sx, sy in steam_positions:
        for i in range(4):
            y = sy - i
            offset = 1 if i % 2 else 0
            if 0 <= y < 32:
                img.putpixel((sx + offset, y), (*steam, 180 - i * 30))

    return add_outline(img)


def make_mini_castle():
    """Mini castle (미니 성)."""
    img = new_sprite(32)
    wall = (200, 190, 170)
    wall_dark = (170, 160, 140)
    roof = (180, 80, 80)
    roof_dark = (150, 55, 55)
    door = (120, 80, 40)
    window = (140, 180, 220)
    flag = (255, 200, 50)

    # Main tower
    fill_rect(img, 10, 10, 22, 28, wall)
    fill_rect(img, 10, 10, 15, 28, wall_dark)

    # Battlements
    for x in range(10, 23, 3):
        fill_rect(img, x, 8, x + 1, 10, wall)

    # Left tower
    fill_rect(img, 4, 6, 10, 28, wall_dark)
    fill_rect(img, 3, 4, 11, 7, roof)

    # Right tower
    fill_rect(img, 22, 6, 28, 28, wall)
    fill_rect(img, 21, 4, 29, 7, roof)

    # Tower tops (pointed)
    fill_rect(img, 5, 2, 8, 4, roof_dark)
    fill_rect(img, 6, 1, 7, 2, roof_dark)
    fill_rect(img, 24, 2, 27, 4, roof_dark)
    fill_rect(img, 25, 1, 26, 2, roof_dark)

    # Door
    fill_rect(img, 14, 22, 18, 28, door)
    fill_rect(img, 14, 22, 18, 23, wall_dark)

    # Windows
    fill_rect(img, 14, 14, 16, 17, window)
    fill_rect(img, 6, 10, 8, 13, window)
    fill_rect(img, 24, 10, 26, 13, window)

    # Flag on left tower
    img.putpixel((7, 0), (*flag, 255))
    fill_rect(img, 7, 0, 11, 1, flag)

    return add_outline(img)


def make_swing():
    """Swing (그네)."""
    img = new_sprite(32)
    frame = (120, 100, 70)
    chain = (180, 180, 185)
    seat = (200, 120, 60)
    seat_light = (220, 150, 90)

    # A-frame top bar
    fill_rect(img, 4, 4, 28, 6, frame)

    # Left A-frame legs
    for i in range(22):
        y = 6 + i
        if y < 30:
            img.putpixel((5 + i // 4, y), (*frame, 255))
            img.putpixel((6 + i // 4, y), (*frame, 255))

    # Right A-frame legs
    for i in range(22):
        y = 6 + i
        if y < 30:
            img.putpixel((27 - i // 4, y), (*frame, 255))
            img.putpixel((26 - i // 4, y), (*frame, 255))

    # Chains
    for y in range(6, 20):
        img.putpixel((13, y), (*chain, 255))
        img.putpixel((19, y), (*chain, 255))

    # Seat
    fill_rect(img, 11, 20, 21, 22, seat)
    fill_rect(img, 12, 19, 20, 20, seat_light)

    return add_outline(img)


def make_slide():
    """Slide (미끄럼틀)."""
    img = new_sprite(32)
    slide_color = (100, 180, 240)
    slide_dark = (70, 150, 210)
    slide_light = (150, 210, 255)
    frame = (180, 180, 185)
    ladder = (160, 160, 165)

    # Slide surface (diagonal)
    for i in range(20):
        x = 8 + i
        y = 8 + int(i * 0.8)
        if 0 <= x < 32 and 0 <= y < 30:
            fill_rect(img, x - 2, y, x + 2, y + 1, slide_color)
            img.putpixel((x - 2, y), (*slide_dark, 255))
            img.putpixel((x + 2, y), (*slide_light, 255))

    # Bottom curve
    fill_rect(img, 26, 24, 30, 26, slide_color)
    fill_rect(img, 28, 24, 30, 28, slide_light)

    # Top platform
    fill_rect(img, 4, 6, 12, 9, frame)

    # Ladder
    fill_rect(img, 4, 9, 5, 28, ladder)
    fill_rect(img, 8, 9, 9, 28, ladder)
    for y in range(11, 28, 3):
        fill_rect(img, 4, y, 9, y, frame)

    # Side rails
    for i in range(16):
        x = 10 + i
        y = 7 + int(i * 0.8)
        if 0 <= x < 32 and 0 <= y < 32:
            img.putpixel((x, y - 2), (*frame, 255))

    return add_outline(img)


def make_aquarium():
    """Aquarium (어항)."""
    img = new_sprite(32)
    glass = (200, 230, 250)
    glass_light = (230, 245, 255)
    water = (120, 190, 230)
    water_dark = (90, 160, 200)
    sand = (220, 200, 150)
    fish = (255, 130, 50)
    plant = (60, 160, 80)
    frame = (160, 160, 165)

    # Tank body
    fill_rect(img, 4, 6, 28, 26, water)
    fill_rect(img, 4, 6, 14, 26, water_dark)

    # Glass shine
    fill_rect(img, 6, 8, 8, 18, glass_light)

    # Sand bottom
    fill_rect(img, 4, 24, 28, 26, sand)

    # Plant
    for y in range(16, 25):
        img.putpixel((22, y), (*plant, 255))
    for pos in [(20, 17), (21, 16), (23, 16), (24, 17)]:
        img.putpixel(pos, (*plant, 255))

    # Fish
    fill_rect(img, 12, 14, 18, 16, fish)
    img.putpixel((11, 15), (*fish, 255))
    img.putpixel((19, 13), (*fish, 255))
    img.putpixel((19, 17), (*fish, 255))
    img.putpixel((14, 14), (20, 20, 20, 255))  # eye

    # Bubbles
    img.putpixel((10, 10), (*glass_light, 255))
    img.putpixel((20, 9), (*glass_light, 255))
    img.putpixel((18, 11), (*glass_light, 255))

    # Frame
    fill_rect(img, 3, 5, 29, 6, frame)
    fill_rect(img, 3, 26, 29, 27, frame)
    fill_rect(img, 3, 5, 4, 27, frame)
    fill_rect(img, 28, 5, 29, 27, frame)

    # Stand
    fill_rect(img, 6, 27, 10, 30, frame)
    fill_rect(img, 22, 27, 26, 30, frame)

    return add_outline(img)


def make_piano():
    """Piano (피아노)."""
    img = new_sprite(32)
    body = (40, 40, 45)
    body_light = (60, 60, 65)
    white_key = (240, 240, 245)
    black_key = (30, 30, 35)
    gold = (200, 180, 80)
    leg = (50, 50, 55)

    # Piano body (upright)
    fill_rect(img, 4, 6, 28, 22, body)
    fill_rect(img, 5, 6, 15, 22, body_light)

    # Top
    fill_rect(img, 3, 4, 29, 7, body)

    # Music stand (open lid)
    fill_rect(img, 6, 2, 26, 5, body_light)

    # White keys
    for x in range(6, 27, 3):
        fill_rect(img, x, 22, x + 2, 26, white_key)
        fill_rect(img, x + 2, 22, x + 2, 26, (200, 200, 205))

    # Black keys
    for x in range(7, 26, 3):
        fill_rect(img, x, 22, x + 1, 24, black_key)

    # Gold pedals
    fill_rect(img, 13, 28, 14, 29, gold)
    fill_rect(img, 16, 28, 17, 29, gold)
    fill_rect(img, 19, 28, 20, 29, gold)

    # Legs
    fill_rect(img, 5, 26, 7, 30, leg)
    fill_rect(img, 25, 26, 27, 30, leg)

    # Music notes
    img.putpixel((10, 1), (80, 80, 80, 255))
    img.putpixel((22, 0), (80, 80, 80, 255))

    return add_outline(img)


def make_tent():
    """Tent (텐트)."""
    img = new_sprite(32)
    fabric = (220, 140, 100)
    fabric_dark = (190, 110, 70)
    fabric_light = (240, 170, 130)
    pole = (160, 160, 165)
    ground = (140, 120, 80)
    inside = (60, 40, 30)

    # Tent body (triangle)
    for row in range(18):
        y = 28 - row
        half_w = int(14 - row * 0.7)
        if half_w > 0:
            x0 = 16 - half_w
            x1 = 16 + half_w
            if x0 < 16:
                fill_rect(img, x0, y, 15, y, fabric_dark)
            if 16 < x1:
                fill_rect(img, 17, y, x1, y, fabric_light)
            img.putpixel((16, y), (*fabric, 255))

    # Door opening (triangle)
    for row in range(8):
        y = 28 - row
        half_w = int(4 - row * 0.4)
        if half_w > 0:
            fill_rect(img, 16 - half_w, y, 16 + half_w, y, inside)

    # Ground line
    fill_rect(img, 2, 28, 30, 29, ground)

    # Pole top
    img.putpixel((16, 10), (*pole, 255))
    img.putpixel((16, 9), (*pole, 255))

    # Flag on top
    fill_rect(img, 17, 8, 20, 10, (255, 200, 80))

    return add_outline(img)


def make_fireplace():
    """Fireplace (벽난로)."""
    img = new_sprite(32)
    brick = (160, 80, 60)
    brick_dark = (130, 55, 40)
    brick_light = (190, 110, 85)
    mantle = (180, 160, 130)
    fire = (255, 160, 30)
    fire_red = (255, 80, 20)
    fire_yellow = (255, 220, 80)
    inside = (40, 30, 25)

    # Brick frame
    fill_rect(img, 4, 6, 28, 28, brick)
    fill_rect(img, 4, 6, 14, 28, brick_dark)

    # Mantle
    fill_rect(img, 2, 4, 30, 7, mantle)

    # Opening
    for row in range(14):
        y = 28 - row
        half_w = int(7 - max(0, row - 8) * 1.5)
        if half_w > 0:
            fill_rect(img, 16 - half_w, y, 16 + half_w, y, inside)

    # Fire
    for row in range(6):
        y = 27 - row
        half_w = 3 - row // 2
        if half_w > 0:
            fill_rect(img, 16 - half_w, y, 16 + half_w, y, fire)
    img.putpixel((16, 21), (*fire_yellow, 255))
    img.putpixel((15, 22), (*fire_red, 255))
    img.putpixel((17, 23), (*fire_red, 255))
    img.putpixel((16, 20), (*fire_yellow, 255))

    # Brick pattern
    for y in range(8, 28, 3):
        for x in range(6, 28, 5):
            px = img.getpixel((x, y))
            if px == (*brick, 255) or px == (*brick_dark, 255):
                img.putpixel((x, y), (*brick_light, 255))

    # Logs
    fill_rect(img, 12, 27, 20, 28, (100, 70, 35))

    return add_outline(img)


def make_chandelier():
    """Chandelier (샹들리에)."""
    img = new_sprite(32)
    gold = (220, 190, 80)
    gold_dark = (180, 150, 50)
    crystal = (200, 220, 250)
    crystal_light = (230, 240, 255)
    chain = (180, 160, 70)
    candle = (255, 250, 230)
    flame = (255, 200, 80)

    # Chain
    for y in range(0, 6):
        img.putpixel((16, y), (*chain, 255))

    # Center hub
    fill_rect(img, 14, 6, 18, 9, gold)

    # Arms
    fill_rect(img, 6, 9, 26, 10, gold)
    fill_rect(img, 6, 10, 6, 12, gold_dark)
    fill_rect(img, 16, 10, 16, 12, gold_dark)
    fill_rect(img, 26, 10, 26, 12, gold_dark)

    # Candles
    for x in [6, 16, 26]:
        fill_rect(img, x - 1, 12, x + 1, 16, candle)
        img.putpixel((x, 11), (*flame, 255))
        img.putpixel((x, 10), (255, 255, 200, 200))

    # Crystals hanging
    for x in [9, 12, 20, 23]:
        for y in range(11, 11 + (x % 5) + 3):
            if 0 <= y < 32:
                img.putpixel((x, y), (*crystal, 255))
        # Crystal tip
        y_end = 11 + (x % 5) + 3
        if y_end < 32:
            img.putpixel((x, y_end), (*crystal_light, 255))

    # Bottom crystal drops
    for x in [10, 14, 18, 22]:
        for dy in range(4):
            y = 17 + dy
            if 0 <= y < 32:
                img.putpixel((x, y), (*crystal, 255))
        if 21 < 32:
            img.putpixel((x, 21), (*crystal_light, 255))

    return add_outline(img)


def make_telescope():
    """Telescope (망원경)."""
    img = new_sprite(32)
    tube = (100, 80, 60)
    tube_light = (140, 115, 85)
    metal = (180, 170, 150)
    lens = (160, 200, 230)
    tripod = (120, 100, 70)

    # Tripod legs
    for i in range(14):
        # Left leg
        img.putpixel((8 + i // 3, 16 + i), (*tripod, 255))
        # Right leg
        img.putpixel((24 - i // 3, 16 + i), (*tripod, 255))
        # Back leg
        img.putpixel((16, 16 + i), (*tripod, 255))

    # Tube body (diagonal, pointing up-right)
    for i in range(16):
        x = 8 + i
        y = 16 - int(i * 0.6)
        for dy in range(-1, 2):
            for dx in range(-1, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 32 and 0 <= ny < 32:
                    if dy == -1:
                        img.putpixel((nx, ny), (*tube_light, 255))
                    else:
                        img.putpixel((nx, ny), (*tube, 255))

    # Lens end
    fill_rect(img, 23, 4, 26, 9, metal)
    fill_rect(img, 24, 5, 25, 8, lens)

    # Eyepiece
    fill_rect(img, 7, 16, 10, 18, metal)

    # Tripod joint
    fill_rect(img, 14, 15, 18, 17, metal)

    return add_outline(img)


def make_carousel():
    """Carousel (회전목마)."""
    img = new_sprite(32)
    pole = (200, 180, 80)
    pole_dark = (170, 150, 50)
    base = (180, 80, 80)
    top = (180, 80, 80)
    horse1 = (240, 220, 200)
    horse2 = (200, 160, 100)
    gold = (255, 220, 100)

    # Center pole
    fill_rect(img, 15, 2, 17, 28, pole)

    # Top canopy
    for row in range(4):
        y = 4 - row
        half_w = 12 - row * 2
        if half_w > 0:
            fill_rect(img, 16 - half_w, y, 16 + half_w, y, top)

    fill_rect(img, 4, 4, 28, 6, base)

    # Top ornament
    img.putpixel((16, 0), (*gold, 255))
    img.putpixel((15, 1), (*gold, 255))
    img.putpixel((17, 1), (*gold, 255))

    # Base platform
    fill_rect(img, 6, 26, 26, 28, base)
    fill_rect(img, 4, 28, 28, 30, pole_dark)

    # Horses (simplified)
    # Left horse
    fill_rect(img, 8, 16, 11, 22, horse1)
    fill_rect(img, 7, 14, 9, 16, horse1)  # head
    fill_rect(img, 8, 22, 8, 25, horse1)  # front leg
    fill_rect(img, 11, 22, 11, 25, horse1)  # back leg
    fill_rect(img, 10, 8, 10, 16, pole)  # pole

    # Right horse
    fill_rect(img, 21, 18, 24, 24, horse2)
    fill_rect(img, 23, 16, 25, 18, horse2)  # head
    fill_rect(img, 21, 24, 21, 26, horse2)
    fill_rect(img, 24, 24, 24, 26, horse2)
    fill_rect(img, 22, 8, 22, 18, pole)  # pole

    return add_outline(img)


def make_rainbow_arch():
    """Rainbow arch (무지개 아치)."""
    img = new_sprite(32)
    import math

    colors = [
        (255, 60, 60),    # red
        (255, 160, 40),   # orange
        (255, 230, 50),   # yellow
        (80, 200, 80),    # green
        (60, 140, 230),   # blue
        (130, 80, 200),   # purple
        (200, 100, 200),  # pink
    ]

    cx, cy = 16, 26

    for i, color in enumerate(colors):
        r_outer = 18 - i * 2
        r_inner = r_outer - 2
        for y in range(32):
            for x in range(32):
                dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
                if r_inner <= dist <= r_outer and y < cy:
                    img.putpixel((x, y), (*color, 255))

    # Pillars at base
    fill_rect(img, 2, 22, 6, 30, (180, 175, 170))
    fill_rect(img, 26, 22, 30, 30, (180, 175, 170))

    # Sparkle at top
    img.putpixel((16, 7), (255, 255, 200, 255))
    img.putpixel((15, 8), (255, 255, 200, 200))
    img.putpixel((17, 8), (255, 255, 200, 200))

    return add_outline(img)


def make_sakura_tree():
    """Sakura/cherry blossom tree (벚꽃나무)."""
    img = new_sprite(32)
    trunk = (120, 80, 50)
    trunk_dark = (90, 55, 30)
    pink = (255, 180, 200)
    pink_dark = (240, 140, 170)
    pink_light = (255, 210, 220)
    petal = (255, 200, 210)

    # Trunk
    fill_rect(img, 14, 18, 18, 30, trunk)
    fill_rect(img, 15, 18, 17, 30, trunk_dark)

    # Branches
    for i in range(4):
        img.putpixel((13 - i, 18 - i), (*trunk, 255))
        img.putpixel((19 + i, 17 - i), (*trunk, 255))

    # Foliage (cherry blossoms - cloud shape)
    centers = [(10, 10), (16, 7), (22, 10), (13, 14), (20, 13)]
    for cx, cy in centers:
        for y in range(32):
            for x in range(32):
                dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
                if dist <= 5:
                    px = img.getpixel((x, y))
                    if px[3] == 0 or px == (*pink, 255) or px == (*pink_dark, 255):
                        if dist > 3.5:
                            img.putpixel((x, y), (*pink_dark, 255))
                        elif y < cy:
                            img.putpixel((x, y), (*pink_light, 255))
                        else:
                            img.putpixel((x, y), (*pink, 255))

    # Falling petals
    import random
    random.seed(42)
    for _ in range(5):
        px = random.randint(4, 28)
        py = random.randint(20, 29)
        if 0 <= px < 32 and 0 <= py < 32:
            img.putpixel((px, py), (*petal, 255))

    return add_outline(img)


def make_golden_bell():
    """Golden bell (황금 방울)."""
    img = new_sprite(32)
    gold = (255, 210, 60)
    gold_dark = (200, 170, 30)
    gold_light = (255, 240, 140)
    slit = (40, 40, 40)
    ring = (220, 180, 40)
    sparkle = (255, 255, 200)
    red_ribbon = (220, 60, 60)

    # Bell body (large sphere)
    cx, cy, r = 16, 17, 10
    for y in range(32):
        for x in range(32):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if dist <= r:
                if x < cx - 3:
                    img.putpixel((x, y), (*gold_dark, 255))
                elif x > cx + 3:
                    img.putpixel((x, y), (*gold_light, 255))
                else:
                    img.putpixel((x, y), (*gold, 255))

    # Bottom slit
    fill_rect(img, 11, 26, 21, 26, slit)
    img.putpixel((16, 27), (*slit, 255))

    # Top loop
    fill_rect(img, 13, 5, 19, 7, ring)
    fill_rect(img, 14, 4, 18, 5, ring)
    fill_rect(img, 15, 6, 17, 6, (0, 0, 0, 0))

    # Ribbon bow
    fill_rect(img, 10, 6, 13, 8, red_ribbon)
    fill_rect(img, 19, 6, 22, 8, red_ribbon)
    fill_rect(img, 14, 7, 18, 8, red_ribbon)

    # Sparkles
    for pos in [(10, 11), (21, 13), (12, 20), (22, 9)]:
        img.putpixel(pos, (*sparkle, 255))

    # Clapper
    img.putpixel((16, 24), (*gold_dark, 255))
    img.putpixel((16, 25), (*gold_dark, 255))

    return add_outline(img)


# ============================================================
# Main generation
# ============================================================

def main():
    import os
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

    # --- Cats ---
    cats = {
        "cat_orange_tabby": {
            "body_color": (230, 160, 60),
            "stripe_color": (180, 110, 30),
            "eye_color": (80, 200, 80),
            "belly_color": (250, 220, 170),
        },
        "cat_black": {
            "body_color": (50, 50, 55),
            "stripe_color": None,
            "eye_color": (220, 200, 50),
            "belly_color": (80, 80, 85),
        },
        "cat_white": {
            "body_color": (240, 240, 245),
            "stripe_color": None,
            "eye_color": (100, 160, 230),
            "belly_color": (255, 255, 255),
        },
        "cat_gray_tabby": {
            "body_color": (150, 150, 155),
            "stripe_color": (100, 100, 105),
            "eye_color": (180, 200, 50),
            "belly_color": (200, 200, 205),
        },
        "cat_calico": {
            "body_color": (240, 230, 210),
            "stripe_color": (200, 120, 50),
            "eye_color": (80, 180, 80),
            "belly_color": (255, 245, 235),
        },
        "cat_siamese": {
            "body_color": (230, 220, 200),
            "stripe_color": None,
            "eye_color": (80, 140, 220),
            "belly_color": (245, 240, 230),
        },
        "cat_russian_blue": {
            "body_color": (130, 145, 165),
            "stripe_color": None,
            "eye_color": (100, 200, 100),
            "belly_color": (170, 185, 200),
        },
        "cat_tuxedo": {
            "body_color": (40, 40, 45),
            "stripe_color": None,
            "eye_color": (180, 200, 50),
            "belly_color": (240, 240, 245),
        },
    }

    print("Generating cat sprites...")
    for name, params in cats.items():
        img = make_cat(
            body_color=params["body_color"],
            stripe_color=params["stripe_color"],
            eye_color=params["eye_color"],
            belly_color=params["belly_color"],
            name=name,
        )
        path = os.path.join(base, "cats", f"{name}.png")
        img.save(path)
        print(f"  ✓ {path}")

    # --- Furballs ---
    print("\nGenerating furball sprites...")
    furballs = {
        "furball_orange": ((230, 160, 60), "medium"),
        "furball_black": ((50, 50, 55), "small"),
        "furball_white": ((235, 235, 240), "medium"),
        "furball_gray": ((150, 150, 155), "large"),
        "furball_calico": ((220, 190, 150), "medium"),
        "furball_golden": ((255, 200, 80), "medium"),
    }

    for name, (color, size) in furballs.items():
        img = make_furball(color, size, name)
        path = os.path.join(base, "furballs", f"{name}.png")
        img.save(path)
        print(f"  ✓ {path}")

    # --- Gacha Items ---
    print("\nGenerating gacha item sprites...")
    gacha_items = {
        "traffic_cone": make_traffic_cone,
        "cat_tower": make_cat_tower,
        "trash_can": make_trash_can,
        "yarn_ball": make_yarn_ball,
        "fish_toy": make_fish_toy,
        "cardboard_box": make_cardboard_box,
        "cushion": make_cushion,
        "food_bowl": make_food_bowl,
        "mouse_toy": make_mouse_toy,
        "plant_pot": make_plant_pot,
        "scratching_post": make_scratching_post,
        "window_perch": make_window_perch,
        # --- Common (16 new) ---
        "newspaper": make_newspaper,
        "paper_bag": make_paper_bag,
        "blanket": make_blanket,
        "water_bowl": make_water_bowl,
        "slipper": make_slipper,
        "tissue_box": make_tissue_box,
        "sock": make_sock,
        "shoe_box": make_shoe_box,
        "milk_carton": make_milk_carton,
        "tin_can": make_tin_can,
        "leaf": make_leaf,
        "pine_cone": make_pine_cone,
        "rubber_duck": make_rubber_duck,
        "ball": make_ball,
        "pencil": make_pencil,
        "plastic_cup": make_plastic_cup,
        # --- Rare (16 new) ---
        "laser_pointer": make_laser_pointer,
        "bell_toy": make_bell_toy,
        "catnip": make_catnip,
        "tunnel": make_tunnel,
        "hammock": make_hammock,
        "feather_wand": make_feather_wand,
        "mirror": make_mirror,
        "music_box": make_music_box,
        "ribbon": make_ribbon,
        "brush": make_brush,
        "treat_jar": make_treat_jar,
        "pillow": make_pillow,
        "rug": make_rug,
        "basket": make_basket,
        "lantern": make_lantern,
        "wind_chime": make_wind_chime,
        # --- Epic (16 new) ---
        "fountain": make_fountain,
        "tree_house": make_tree_house,
        "hot_spring": make_hot_spring,
        "mini_castle": make_mini_castle,
        "swing": make_swing,
        "slide": make_slide,
        "aquarium": make_aquarium,
        "piano": make_piano,
        "tent": make_tent,
        "fireplace": make_fireplace,
        "chandelier": make_chandelier,
        "telescope": make_telescope,
        "carousel": make_carousel,
        "rainbow_arch": make_rainbow_arch,
        "sakura_tree": make_sakura_tree,
        "golden_bell": make_golden_bell,
    }

    for name, gen_func in gacha_items.items():
        img = gen_func()
        path = os.path.join(base, "gacha_items", f"{name}.png")
        img.save(path)
        print(f"  ✓ {path}")

    print(f"\n🎉 All assets generated! Total: {len(cats)} cats, {len(furballs)} furballs, {len(gacha_items)} gacha items")


if __name__ == "__main__":
    main()
