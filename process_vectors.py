import re
import os
import vtracer
from PIL import Image, ImageFilter
import numpy as np

# 1. Load original screenshot
img = Image.open(r'C:/Users/knafl/.gemini/antigravity/brain/96125b61-03b2-4cc6-aa58-9073f970c642/.user_uploaded/media_1791991856680_e20e64bf.png').convert('RGB')
sq = img.crop((18, 12, 156, 150))
knot = sq.crop((10, 10, 128, 128))

# 2. Resize to 1024x1024
knot_1024 = knot.resize((1024, 1024), Image.Resampling.LANCZOS)
arr = np.array(knot_1024.convert('L'))

# In knot_1024, background is white (>180), lines are dark (<120)
knot_inv = np.where(arr < 135, 255, 0).astype(np.uint8)
Image.fromarray(knot_inv).save('public/temp_knot_inv.png')

vtracer.convert_image_to_svg_py('public/temp_knot_inv.png', 'public/temp_knot_inv.svg')

with open('public/temp_knot_inv.svg', 'r', encoding='utf-8') as f:
    svg_raw = f.read()

pattern = re.compile(r'<path d="([^"]+)" fill="([^"]+)"([^>]*)/>')
matches = pattern.findall(svg_raw)

# Filter out the 1024x1024 background box (len 169)
knot_paths = []
for d, fill, rest in matches:
    if len(d) > 200:
        knot_paths.append((d, rest))

print(f"Extracted {len(knot_paths)} actual knot spline paths!")

# Construct pure vector SVG (default fill="currentColor")
svg_pure = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="100%" height="100%" fill="currentColor">\n'
for d, rest in knot_paths:
    svg_pure += f'  <path d="{d}" {rest}/>\n'
svg_pure += '</svg>'

with open('public/quatra-knot.svg', 'w', encoding='utf-8') as f:
    f.write(svg_pure)

with open('public/quatra-knot-white.svg', 'w', encoding='utf-8') as f:
    f.write(svg_pure.replace('fill="currentColor"', 'fill="#FFFFFF"'))

with open('public/quatra-knot-black.svg', 'w', encoding='utf-8') as f:
    f.write(svg_pure.replace('fill="currentColor"', 'fill="#000000"'))

# Squircle Badge SVG (Pure vector white card with black knot)
svg_badge = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="100%" height="100%">
  <rect width="1024" height="1024" rx="256" fill="#FFFFFF"/>
  <g transform="translate(102.4, 102.4) scale(0.8)" fill="#000000">
'''
for d, rest in knot_paths:
    svg_badge += f'    <path d="{d}" {rest}/>\n'
svg_badge += '  </g>\n</svg>'

with open('public/quatra-badge.svg', 'w', encoding='utf-8') as f:
    f.write(svg_badge)

# Dark Squircle Badge SVG
svg_badge_dark = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="100%" height="100%">
  <rect width="1024" height="1024" rx="256" fill="#0A0A0A" stroke="#262626" stroke-width="16"/>
  <g transform="translate(102.4, 102.4) scale(0.8)" fill="#FFFFFF">
'''
for d, rest in knot_paths:
    svg_badge_dark += f'    <path d="{d}" {rest}/>\n'
svg_badge_dark += '  </g>\n</svg>'

with open('public/quatra-badge-dark.svg', 'w', encoding='utf-8') as f:
    f.write(svg_badge_dark)

# Ultra-HD 2048x2048 PNGs
knot_2048 = knot.resize((2048, 2048), Image.Resampling.LANCZOS)
k_arr = np.array(knot_2048.convert('L')).astype(float)
alpha_2048 = np.clip((245.0 - k_arr) / (245.0 - 50.0) * 255.0, 0, 255).astype(np.uint8)

png_black = np.zeros((2048, 2048, 4), dtype=np.uint8)
png_black[..., 3] = alpha_2048
Image.fromarray(png_black, 'RGBA').save('public/quatra-knot-black-2048.png')

png_white = np.full((2048, 2048, 4), 255, dtype=np.uint8)
png_white[..., 3] = alpha_2048
Image.fromarray(png_white, 'RGBA').save('public/quatra-knot-white-2048.png')

from PIL import ImageDraw
mask = Image.new('L', (2048, 2048), 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle((0, 0, 2048, 2048), radius=512, fill=255)
badge_2048 = Image.new('RGBA', (2048, 2048), (255, 255, 255, 255))
badge_2048.putalpha(mask)

black_scaled = Image.fromarray(png_black, 'RGBA').resize((1600, 1600), Image.Resampling.LANCZOS)
badge_2048.paste(black_scaled, (224, 224), black_scaled)
badge_2048.save('public/quatra-badge-2048.png')

# Site assets
badge_2048.resize((552, 552), Image.Resampling.LANCZOS).save('public/quatra-badge-hd.png')
badge_2048.resize((256, 256), Image.Resampling.LANCZOS).save('public/quatra-app-icon.png')
badge_2048.resize((64, 64), Image.Resampling.LANCZOS).save('public/favicon.png')
Image.fromarray(png_white, 'RGBA').resize((512, 512), Image.Resampling.LANCZOS).save('public/quatra-symbol-white.png')
Image.fromarray(png_white, 'RGBA').resize((512, 512), Image.Resampling.LANCZOS).save('public/quatra-knot-white.png')

# Clean temp
if os.path.exists('public/temp_knot_inv.png'): os.remove('public/temp_knot_inv.png')
if os.path.exists('public/temp_knot_inv.svg'): os.remove('public/temp_knot_inv.svg')

print("SUCCESS: 24 vector spline paths and 2048px Ultra-HD PNGs created!")
