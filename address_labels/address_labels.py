# create address labels 

the_format = open("Format.txt", "r")
data = open("Data.txt", "r")

to = the_format.readline().rstrip()
address = the_format.readline()

the_format.close()

for to_field in data:
    print(f"{to} {to_field}{address}{next(data)}")

data.close()