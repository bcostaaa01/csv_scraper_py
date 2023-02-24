import csv

def main(params):
    input_filename, output_filename = params["input"], params["output"]

    # open the CSV file
    with open(input_filename) as input_file:
        # create a CSV reader object
        csv_reader = csv.reader(input_file)

        with open(output_filename, mode='w', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            # iterate over each row in the CSV file
            for row in csv_reader:
                # write new CSV file with value of row[2]
                value = row[2]

                csv_writer.writerow([value])

params = {
    "input": "people-100.csv",
    "output": "newFile.csv",
}
main(params)
