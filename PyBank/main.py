import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")

with open (budget_data) as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)


    # these are the various data points we're looking for
    # some of them are used to calculate further data points
    number_of_months = 0
    total_profits = 0
    previous_row_profit = 0
    monthly_changes = []
    average_daily_change = int()
    greatest_increase = int()
    greatest_decrease = int()

    for row in csvreader:
        monthly_profit = int(row[1])
        
        number_of_months += 1

        total_profits += monthly_profit

        monthly_change = monthly_profit - previous_row_profit
       
        monthly_changes.append(monthly_change)
       
        previous_row_profit = monthly_profit
        

    #This will be our big print statement
    print(number_of_months)
    print(total_profits)

    #Here I'll put the thing to make a .txt file