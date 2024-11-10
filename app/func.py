import aiohttp
from PIL import Image
import base64
from io import BytesIO
from app.bot import bot
from config_file.cfg import token

async def download_file(file_url: str, file_name: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as resp:
            with open(file_name, 'wb') as f:
                f.write(await resp.read())

def decode_image(img_base64):
    img_data = base64.b64decode(img_base64)
    img = Image.open(BytesIO(img_data))
    return img

def encode_image(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_base64

def rotate_photo_on_the_right(img_base64):
    img = decode_image(img_base64).rotate(-90, expand=True)
    return encode_image(img)

def rotate_photo_on_the_left(img_base64):
    img = decode_image(img_base64).rotate(90, expand=True)
    return encode_image(img)

def rotate_photo_upside_down(img_base64):
    img = decode_image(img_base64).rotate(180, expand=True)
    return encode_image(img)

async def get_photo(file_id):
    file = await bot.get_file(file_id)
    file_path = file.file_path
    url = f'https://api.telegram.org/file/bot{token}/{file_path}'
    return url

def load_image(file_path):
    return Image.open(file_path)
