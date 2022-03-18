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
            id.line((randint(1, 300), randint(1, 100), randint(1, 300), randint(1, 100)), fill=128)
    font_large = ImageFont.truetype("fonts/DejaVuSansMono.ttf", size=20)
    x, y = (120+(randint(-2,2)*10), 40+(randint(-2,2)*10))
    id.text((x, y), key, font=font_large, fill=(0, 0, 0))
    
    img.putpixel((0, y), 0)
    img.putpixel((x, 0), 0)

    img.save(data, format="PNG")
    data.seek(0)
    return ("data:image/png;base64,"+b64encode(data.getvalue()).decode("ascii"), key)