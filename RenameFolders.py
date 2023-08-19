import os


def rename(dir, file_list, prefix):
    dir = input("Choose the directory: ")

    file_list = os.listdir(dir)

    prefix = input("The prefix: ")

    for filename in file_list:
        new_name = prefix + filename
        old_path = os.path.join(dir, filename)
        new_path = os.path.join(dir, new_name)
        os.rename(old_path, new_path)

rename("", "")