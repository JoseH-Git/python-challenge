# Import Modules

import os
import csv
import sys

total_voters = []
candidates = []

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Loop through lookin
    #print(f"CSV Header: {csv_header}")
    
    # Loop through lookin
    for row in csvreader:
        total_voters.append(row[0])
        candidates.append(row[2])
        #candidate_count = int(candidates[row])
        #total_months = len(total_month)
        #total_month_amount = sum(total_profit)
        #average = float(total_month_amount / total_months)
    
    new_candidates = list(set(candidates))
    total_candidates = len(new_candidates)
    #candidate_count = new_candidates.count[0]

    
    print("Election Results")
    print("-------------------------")
    print("Total Voters: " + str(len(total_voters)))
    print("-------------------------")
    for i in range(total_candidates):
        #print(new_candidates[i] + " (" +str(candidates.count(new_candidates[i])) +")")
        candidate1 = new_candidates[i]
        total_candidate1 = candidates.count(new_candidates[i])
        print(candidate1 +" "+ str(round((total_candidate1)*100/(len(total_voters)))) + "% " + str(total_candidate1))
        #print(round((total_candidate1)*100/(len(total_voters))))
    #print(new_candidates[0]+": " + "("+ str(candidates.count("Khan")) + ")")
    #print(new_candidates[1]+": " + "("+ str(candidates.count("O'Tooley")) + ")")
    #print(new_candidates[2]+": " + "("+ str(candidates.count("Correy")) + ")")
    #print(new_candidates[3]+": " + "("+ str(candidates.count("Li")) + ")")
    #print("-------------------------")
    #print(total_candidates)