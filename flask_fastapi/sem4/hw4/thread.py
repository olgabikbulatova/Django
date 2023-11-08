import argparse
import os
import requests
import time
import threading


# urls = [
#     'https://images.wallpaperscraft.ru/image/single/zelenyj_piton_piton_zmeia_971009_3840x2400.jpg',
#     'https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-22.jpg',
#     'https://wallpapers.com/images/hd/venomous-red-eyed-green-snake-80kf9kmun58os630.jpg',
#     'https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-42.jpg',
#     'https://fun-cats.ru/wp-content/uploads/a/3/e/a3e758db8d5f9091d7b88a7ede20b556.jpeg',
# ]


def get_img(url):
    img_data = requests.get(url).content
    filename = os.path.basename(url)
    with open(f'thread/{filename}', "wb") as f:
        f.write(img_data)
    print(f"Downloaded {filename} in {time.time() - start_time:.2f}seconds")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IMG_url')
    parser.add_argument('url', metavar='U', type=str, nargs='*', help='enter img_url')
    args = parser.parse_args()
    threads = []
    start_time = time.time()
    for url in args.url:
        thread = threading.Thread(target=get_img, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    finish_time = time.time()
    print(f"Общее время выполнения программы {finish_time - start_time:.2f}seconds")


