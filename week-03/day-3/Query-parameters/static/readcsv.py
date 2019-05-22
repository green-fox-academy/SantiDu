import csv

with open("products.csv") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        print(row['name'], row['price'])