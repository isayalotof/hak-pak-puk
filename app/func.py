import aiohttp


async def download_file(file_url: str, file_name: str):
    # Скачиваем фото с использованием aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as resp:
            with open(file_name, 'wb') as f:
                f.write(await resp.read())


