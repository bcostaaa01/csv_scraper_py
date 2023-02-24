import csv
import argparse

def main(args):
    input_filename, output_filename = args.input, args.output

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

# For docs see: 
# https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(
    prog = "csv_scraper.py",
    description = "parse an input CSV file, process and output to a separate file"
)

# Both arguments are optional and non-positional
parser.add_argument('--input', required=False, default="people-100.csv")
parser.add_argument('--output', required=False, default="newFile.csv")

args = parser.parse_args()
main(args)
