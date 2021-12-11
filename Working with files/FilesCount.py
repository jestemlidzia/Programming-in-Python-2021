import os

def filesCount(path):
    dir_list = os.listdir(path)

    print("Number of files in '", path, "' :")

    counter = len(
        [name for name in dir_list if os.path.isfile(os.path.join(path, name))])

    print(counter)

path = "D:/PRIVATE/do nauki/kody/Python/Python"
filesCount(path)