import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")

with open (budget_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)

    for row in csvreader:
        print(row)