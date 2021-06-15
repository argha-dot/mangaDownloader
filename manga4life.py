import os, sys, shutil
import requests

from zipfile import ZipFile
from datetime import date


def get_all_file_paths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def download_chapter_mfl(url, chapter, manga_name, final_page=100000):
    
    initial_page = 1
    folder_name = f"{manga_name}/{manga_name} {chapter} ({date.today().year}) (Digital)"
    os.makedirs(f"{folder_name}", exist_ok=True)

    try:
        for i in range(initial_page, final_page + 1):
            url_img = f"{url}{str(chapter).zfill(4)}-{str(i).zfill(3)}.png"
            r = requests.get(url_img)

            try:
                r.raise_for_status()
            except Exception as e:
                print(f"[ALL IMAGES DOWNLOADED], moving onto the next step")
                break

            file_name = f"{str(chapter).zfill(4)}_{str(i).zfill(3)}.png"
            
            try:
                with open(os.path.join(folder_name, file_name), "wb") as f:
                    f.write(r.content)
                    print(f"[DONE] {file_name} ({url_img})")

            except Exception as e:
                raise print(f"Couldn't write {file_name}, {e} occured!")

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

        print(f"\n\t\t---CHAPTER {chapter} DONE---\t\t\n")


    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, cleaning up...")
        sys.exit(1)


def main():
    url = input("Link: ").strip()
    chapter = int(input("Chapter: "))
    manga_name = input("Manga Name: ").strip()


    download_chapter_mfl(url, chapter, manga_name)


if __name__ == "__main__":
    main()
