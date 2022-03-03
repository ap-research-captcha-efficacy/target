from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from base64 import b64encode
from secrets import token_hex

def generate(mod):
    key = token_hex(3)

    data = BytesIO()

    img = Image.new(mode="RGB", size=(300, 100), color=(255, 255, 255))
    id = ImageDraw.Draw(img)
    font_large = ImageFont.truetype("fonts/DejaVuSansMono.ttf", size=20)
    id.text((0, 0), key, font=font_large, fill=(55, 55, 55))
    
    img.save(data, format="PNG")
    data.seek(0)
    return ("data:image/png;base64,"+b64encode(data.getvalue()).decode("ascii"), key)