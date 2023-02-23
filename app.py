import csv

with open('filename.csv') as file:
    # create a CSV reader object
    csv_reader = csv.reader(file)

    # iterate over each row in the CSV file
    for row in csv_reader:
        print(row)
