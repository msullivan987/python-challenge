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
    previous_row_profit = None
    monthly_changes = []
    monthly_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    best_month = str()
    worst_month = str()

    for row in csvreader:
        #set monthly profit to the current row's profit
        monthly_profit = int(row[1])
        
        #find the total number of months
        number_of_months += 1

        #add current monthly profit to total profit
        total_profits += monthly_profit

        #create a list of monthly changes starting with the second month 
        if previous_row_profit is not None:
            monthly_change = monthly_profit - previous_row_profit
       
            monthly_changes.append(monthly_change)

        #next two if statements store greatest and smallest changes
        if monthly_change >  greatest_increase:
            greatest_increase = monthly_change
            best_month = row[0]
        
        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            worst_month = row[0]
       
        #keep track of the profit for this row to use next loop
        previous_row_profit = monthly_profit
        
    def average(numbers_list):
        length = len(numbers_list)
        total = 0
        for number in numbers_list:
            total += number
        return total/length


    #Final analysis and print statement
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {number_of_months}")
    print("Total: $" + str(round(total_profits)))
    print("Average Change: $" + str(round(average(monthly_changes),2)))
    print(f"Greatest Increase in Profits: {best_month} (${greatest_increase})") 
    print(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})")
    
    #Create a txt file with the financial analysis

    file = open(os.path.join("Analysis","financial_analysis.txt"),"w")

    file.write("Financial Analysis \n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {number_of_months}\n")
    file.write("Total: $" + str(round(total_profits)) + "\n")
    file.write("Average Change: $" + str(round(average(monthly_changes),2)) + "\n")
    file.write(f"Greatest Increase in Profits: {best_month} (${greatest_increase})\n") 
    file.write(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})\n")
    
    file.close()