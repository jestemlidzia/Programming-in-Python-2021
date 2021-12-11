import json

file = open('database.json')
database = json.load(file)


def write_data(none=0):
    with open('database.json', 'w') as file:
        json.dump(database, file, indent=4)

def read_data():
    with open('database.json') as json_file:
        data = json.load(json_file)
        for p in data['Songs']:
            print('Title: ' + p['Title'])
            print('Artist: ' + p['Artist'])
            print('Album: ' + p['Album'])
            print('Year: ' + str(p['Year']))
            print('')

def json_example():

    action = input("Choose activity:\n\t1. Display songs \n\t2. Add new song \n\t3. Remove song\n")

    match action:
        case "1":
            read_data()
        case "2":
            name = input("Title: ")
            artist = input("Artist: ")
            album = input("Album: ")
            year = int(input("Year: "))

            song={
                "Title" : name,
                "Artist" : artist,
                "Album" : album,
                "Year" : year
            }

            database['Songs'].append(song)
            write_data(database)
        case "3":
            R_song = input("Which song do you want delete? input song title")

            j = 0
            for i in database['Songs']:
                if i['Title'] == str(R_song):
                    del database['Songs'][j]
                j=j+1
            
            write_data(database)
        case _:
            print("Wybierz jeszcze raz")

json_example()