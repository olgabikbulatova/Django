import argparse
import asyncio
import os
import aiohttp
import time


# urls = ['https://images.wallpaperscraft.ru/image/single/zelenyj_piton_piton_zmeia_971009_3840x2400.jpg',
#         'https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-22.jpg',
#         'https://wallpapers.com/images/hd/venomous-red-eyed-green-snake-80kf9kmun58os630.jpg',
#         'https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-42.jpg',
#         'https://fun-cats.ru/wp-content/uploads/a/3/e/a3e758db8d5f9091d7b88a7ede20b556.jpeg',
#         ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img = await response.read()
            filename = os.path.basename(url)
            with open(f'hw4/async/{filename}', "wb") as f:
                # img = await response.content.read()
                f.write(img)
            print(f"Downloaded {filename} in {time.time() - start_time:.2f} seconds")


parser = argparse.ArgumentParser(description='IMG_url')
parser.add_argument('url', metavar='U', type=str, nargs='*', help='enter img_url')
args = parser.parse_args()


async def main():
    tasks = []
    for url in args.url:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
        await asyncio.gather(*tasks)

start_time = time.time()
if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    finish_time = time.time()
    print(f"Общее время выполнения программы {finish_time - start_time:.2f}seconds")

