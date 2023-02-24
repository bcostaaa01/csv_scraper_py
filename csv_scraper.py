import csv

# open the CSV file
with open('people-100.csv') as input_file:
    # create a CSV reader object
    csv_reader = csv.reader(input_file)

    with open('newFile.csv', mode='w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        # iterate over each row in the CSV file
        for row in csv_reader:
            # write new CSV file with value of row[2]
            value = row[2]

            csv_writer.writerow([value])
