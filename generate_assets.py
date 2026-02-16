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
# Main generation
# ============================================================

def main():
    import os
    base = "/home/user/furrball-collector/assets"

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
    }

    for name, gen_func in gacha_items.items():
        img = gen_func()
        path = os.path.join(base, "gacha_items", f"{name}.png")
        img.save(path)
        print(f"  ✓ {path}")

    print(f"\n🎉 All assets generated! Total: {len(cats)} cats, {len(furballs)} furballs, {len(gacha_items)} gacha items")


if __name__ == "__main__":
    main()
