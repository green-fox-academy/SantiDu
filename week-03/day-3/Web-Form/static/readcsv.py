import csv

def queryProducts(data, field):
    with open("./products.csv") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        output = []
        for row in reader:
            if field in ["qty", "price"]:
                if row[field] == data:
                    output.append(row)
            else:
                if data in row[field]:
                    output.append(row)
        print(output) 

queryProducts("display", "name")