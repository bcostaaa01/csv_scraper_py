# :file_folder: CSV Scraper

This Python script demonstrates how to scrape data from a CSV file using the built-in `csv` module in Python.

## :rocket: Usage

1. Make sure you have Python installed on your computer.
2. Download the `csv_scraper.py` file and place it in the same directory as your CSV file.
3. In a terminal or command prompt, navigate to the directory where the `csv_scraper.py` file is located.
4. Run the following command: `python csv_scraper.py your_file_name.csv`, replacing `your_file_name.csv` with the name of your CSV file.
5. The script will read each row of the CSV file and print it to the console.

## :bulb: Example

Suppose you have a CSV file named `data.csv` with the following contents:

```
Name, Age, Gender, Status
Joost, 21, Male, In a relationship
Lotte, 20, Female, In a relationship

```

You can use the `csv_scraper.py` script to read this file by running the command `python csv_scraper.py data.csv` in your terminal or command prompt. The script will output the following to the console:

```
['Name', ' Age', ' Gender', 'Status']
['Joost', ' 21', ' Male', 'In a relationship']
['Lotte', ' 20', ' Female', 'In a relationship']

```

## :scroll: License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
