import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")



with open (budget_data) as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)

    # for row in csvreader:
    #     print(row)

    number_of_months = int()

    total_profits = int()

    for row in csvreader:
        
        number_of_months = number_of_months + 1

        total_profits = total_profits + int(row[1])

    print(number_of_months)
    print(total_profits)