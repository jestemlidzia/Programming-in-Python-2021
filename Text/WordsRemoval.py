import os

word_list = ["się", " i ", "oraz", "nigdy", "dlaczego"]
with open("Mazury.txt") as input_file, open("MazuryCopy.txt", "w+") as output_file:
    for line in input_file:
        for word in word_list:
            line = line.replace(word, "")
        output_file.write(line)