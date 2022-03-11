from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from base64 import b64encode
from secrets import token_hex
from random import randint

valid_mods = ["obstruct"]

def generate(mod):
    print(mod)
    key = token_hex(3)

    data = BytesIO()
    img = Image.new(mode="RGB", size=(300, 100), color=(255, 255, 255))
    id = ImageDraw.Draw(img)
    if mod and "obstruct" in mod:
        for i in range(0, 10):
            id.line((randint(0, 300), randint(0, 100), randint(0, 300), randint(0, 100)), fill=128)
    font_large = ImageFont.truetype("fonts/DejaVuSansMono.ttf", size=20)
    id.text((120+randint(-20,20), 40+randint(-20,20)), key, font=font_large, fill=(0, 0, 0))
    
    img.save(data, format="PNG")
    data.seek(0)
    return ("data:image/png;base64,"+b64encode(data.getvalue()).decode("ascii"), key)