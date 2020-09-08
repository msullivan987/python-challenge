import os
import csv

election_data = os.path.join("Resources","election_data.csv")

votes = 0
winner = str()

with open (election_data) as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)

    for row in csvreader:
        votes += 1

    
    #Printing results to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votes}")
    print("-------------------------")
    print("-------------------------")
    print(f"Winner: ")
    print("-------------------------")

