import sys
import os
import shutil
from datetime import date
from zipfile import ZipFile

from requests_html import HTMLSession
import requests

def get_all_file_paths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def get_urls(url, chapter):
    img_urls = []

    try:
        session = HTMLSession()
        r = session.get(f"{url}chapter_{chapter}")
        r.html.render()

        res = r.html.find('img[data-src]')

        for img in res:
            img_urls.append(img.attrs["data-src"])

    except Exception as e:
        raise print(f"Couldn't get urls {e} occured!")
        sys.exit(1)

    return img_urls


def download_images(urls, chapter, folder_name):
    for i, url in enumerate(urls):
        r = requests.get(url)
        r.raise_for_status()

        file_name = f"{str(chapter).zfill(4)}_{str(i).zfill(3)}.png"

        try:
            with open(os.path.join(folder_name, file_name), "wb") as f:
                f.write(r.content)
                print(f"[DONE] {file_name} ({url})")

        except Exception as e:
            raise print(f"Couldn't write {file_name}, {e} occured!")


def create_folder(manga_name, chapter):
    folder_name = f"{manga_name}/{manga_name} {chapter} ({date.today().year}) (Digital)"
    try:
        os.makedirs(folder_name, exist_ok=True)

    except Exception as e:
        raise print(f"Couldn't create folder {e} occured!")

    return folder_name


def zip_rename_delete(folder_name):
    try:
        file_paths = get_all_file_paths(folder_name)
        with ZipFile(f"{folder_name}.zip", "w") as zip_file:
            for file in file_paths:
                zip_file.write(f"{file}")

        print("[FILE ZIPPED]", f"{folder_name}.zip")
    except Exception as e:
        raise e

    try:
        os.rename(f"{folder_name}.zip", f"{folder_name}.cbz")
        print("[FILE RENAMED]", f"{folder_name}.zip to {folder_name}.cbz")
    except Exception as e:
        raise e

    try:
        shutil.rmtree(folder_name)
        print("[FOLDER REMOVED]", f"{folder_name}/")
    except Exception as e:
        raise e


def download_chapter_mkk(url, chapter, manga_name):
    urls = get_urls(url, chapter)
    folder_name = create_folder(manga_name, chapter)
    download_images(urls, chapter, folder_name)
    zip_rename_delete(folder_name)

    print(f"\n\t\t---CHAPTER {chapter} DONE---\t\t\n")


def main():
    url = input("Link: ").strip()
    chapter = int(input("Chapter: "))
    manga_name = input("Manga Name: ").strip()

    download_chapter_mkk(url, chapter, manga_name)


if __name__ == "__main__":
    main()
