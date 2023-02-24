# :file_folder: CSV Scraper

This Python script demonstrates how to scrape data from a CSV file using the built-in `csv` module in Python.

## :rocket: Usage

1. Make sure you have Python installed on your computer.
2. Download the `csv_scraper.py` file and place it in the same directory as your CSV data and newFile.csv files are located.
3. In a terminal or command prompt, navigate to the directory where the `csv_scraper.py` file is located.
4. Run the following command: `python csv_scraper.py your_file_name.csv`, replacing `your_file_name.csv` with the name of your CSV file.

To extract the values in the third column (indexed as 2) of each row and write them to a new CSV file, you can modify the script as follows:

1. The script opens the input CSV file and creates a CSV reader object.
2. It then opens the output CSV file and creates a CSV writer object.
3. For each row in the input CSV file, it extracts the value in the third column and writes it to the output CSV file as a new row.

## :bulb: Example

Suppose you have a CSV file named `data.csv` with the following contents:

```
Name, Age, Gender, Status
Joost, 21, Male, In a relationship
Lotte, 20, Female, In a relationship

```

If you now go into `newFile.csv`, you will find the following data:

```
[' Gender']
[' Male']
[' Female']

```

You can modify the `csv_scraper.py` to your specific needs, for example if you would like to render the 1st element in the CSV file:

```python
for row in csv_reader:
    # write new CSV file with value of row[2]
    value = row[0]

    csv_writer.writerow([value])
```

This would then have the following data on `newFile.csv`:

```
[' Name']
[' Joost']
[' Lotte']
```

## :scroll: License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
