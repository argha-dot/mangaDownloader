import sys

from manga4life import download_chapter_mfl
from mangakalot import download_chapter_mkk
from prompts import prompts


def get_every(url, site, start_chapter, end_chapter, manga_name, point_five=False):
    for chapter in range(start_chapter, end_chapter + 1):
        try:
            if site == "manga4life":
                download_chapter_mfl(url, chapter, manga_name)

                if point_five:
                    download_chapter_mfl(url, f"{chapter}.5", manga_name, 1)

            elif site == "mangakakalot":
                download_chapter_mkk(url, chapter, manga_name)

        except Exception as e:
            print(f"{e} Link's probably changed")
            break

    print(f"ALL CHAPTERS DOWNLOADED")


def main():
    answers = prompts()

    get_every(answers['url'], answers['site'], int(answers['start_chapter']),
              int(answers['end_chapter']), answers['manga_name'], int(answers['point_five']))


if __name__ == "__main__":
    main()
    input("\t\tPRESS ANY BUTTON TO EXIT")
