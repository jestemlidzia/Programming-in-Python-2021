import os

path = "D:/PRIVATE/do nauki/kody/Python"


def directory_tree(directory, offset):
    for name in os.listdir(directory):

        current_path = os.path.join(directory, name)
        print(offset, ">", current_path)

        if os.path.isdir(current_path):
            directory_tree(current_path, offset + "---")


directory_tree(path, "")
