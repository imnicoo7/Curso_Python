import csv

with open("archivo.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
