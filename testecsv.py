import csv
with open('./bdados/nivel.csv', 'r') as file:
    reader = csv.reader(file)
    for column in reader:
        print(column)
