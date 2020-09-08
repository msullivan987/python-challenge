import os
import csv

election_data = os.path.join("Resources","election_data.csv")

votes = 0
winner = str()
candidate_dict = {}

with open (election_data) as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter = ",")

    csv_header = next(csvreader)
    
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
    
    #loop through candidate dicionary
    for candidate , vote_count in candidate_dict.items():
        print(f"{candidate}: " + str("{0:.3%}".format(vote_count/votes)) + f" ({vote_count})")
    print("-------------------------")
    
    #find the winner of the election
    winner = max(candidate_dict, key=candidate_dict.get)
    print(f"Winner: {winner}")
    print("-------------------------")


    #create a text file with the election data

    file = open(os.path.join("Analysis","election_results.txt"),"w")

    file.write("Election Results \n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {votes}\n")
    file.write("-------------------------\n")
    
    for candidate , vote_count in candidate_dict.items():
        file.write(f"{candidate}: " + str("{0:.3%}".format(vote_count/votes)) + f" ({vote_count})\n")
    file.write("-------------------------\n")
    
    winner = max(candidate_dict, key=candidate_dict.get)
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
    
    file.close()