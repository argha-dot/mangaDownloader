import os, sys, shutil, zipfile, pprint, time, re


def get_all_file_paths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def extract_all_files(file_list, folder_name):
    for file in file_list:
        try:
            with zipfile.ZipFile(file) as z:
                z.extractall(folder_name)
                print(f"[FILE EXTRACTED] {file}")
        except Exception as e:
            print(e)


def zip_em_up(folder):
    try:
        file_paths = get_all_file_paths(folder)
        with zipfile.ZipFile(f"{folder}.zip", "w") as zip_file:
            for file in file_paths:
                zip_file.write(f"{file}")

        print("[FILE ZIPPED]", f"{folder}.zip")
    except Exception as e:
        raise e


def main():
    
    file_list = get_all_file_paths(".")
    file_list.remove(".\\fix.py")

    extract_all_files(file_list, ".")


if __name__ == "__main__":
    main()