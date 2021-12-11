import os

word_dictonary = {'i': 'oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy',
                       'dlaczego': 'czemu'}

with open("Mazury.txt") as input_file, open("MazuryCopy2.txt", "w+") as output_file:
    lines = input_file.read().split()
    for i in lines:
        for word in word_dictonary.keys():
            if(word == i):
                i = word_dictonary.get(word)
        i=i+" "
        output_file.write(i)
                


