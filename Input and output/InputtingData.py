input_data = input(
    "Enter youame, surname and date of birth in format: NAME SURNAME YEAR: ")

x = input_data.split()

if(len(x) != 3):
    print("Incorrect input")
else:
    print("Name: ", x[0])
    print("Surname ", x[1])
    print("Year od birth: ", x[2])
