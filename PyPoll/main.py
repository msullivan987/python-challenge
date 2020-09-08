import os
import csv

election_data = os.path.join("Resources","election_data.csv")

votes = 0
winner = str()
candidate_dict = {}
candidate_list = []

with open (election_data) as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)
  
    candidate_number = 0
    
    for row in csvreader:
        
        #count up the total votes
        votes += 1
        
        #add new candidates to dictionary
        #give them one vote
        candidate = row[2]
        if candidate not in candidate_dict:
            
            candidate_dict[candidate] = 1
        
        #update current candidate dict value by adding 1
        else:
            candidate_dict[candidate] = candidate_dict[candidate] + 1
    
    #Printing results to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {votes}")
    print("-------------------------")
    print(candidate_dict)
    print("-------------------------")
    print(f"Winner: ")
    print("-------------------------")

