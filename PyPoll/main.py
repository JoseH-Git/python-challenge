# Import Modules

import os
import csv
import sys

# Create Lists to determine total voters and candidates

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
    
    # Loop through CSV file to fill Lists:
    for row in csvreader:
        total_voters.append(row[0])
        candidates.append(row[2])

    # Calculate candidates and total votes:

    new_candidates = list(set(candidates))
    total_candidates = len(new_candidates)
    total_votes = []
    percentage = []
    candidates_dic = {"names": new_candidates, "votes": total_votes, "percentage": percentage}

    print("Election Results")
    print("-------------------------")
    print("Total Voters: " + str(len(total_voters)))
    print("-------------------------")
    for i in range(total_candidates):
        candidates_dic ["names"] = new_candidates[i]
        candidates_dic ["votes"] = candidates.count(new_candidates[i])
        candidates_dic ["percentage"] = str(round(candidates_dic ["votes"]*100/(len(total_voters)),2))
        print(f'{candidates_dic["names"]}: {candidates_dic["percentage"]}% ({candidates_dic["votes"]})')
    print("-------------------------")
    print("Winner:"+ candidates_dic["names"] + " " + max(candidates_dic["percentage"])) 
    print("-------------------------")

    #Redirect Print to .txt

    sys.stdout=open("../analysis/main_output.txt","w")
    print("Election Results")
    print("-------------------------")
    print("Total Voters: " + str(len(total_voters)))
    print("-------------------------")
    for i in range(total_candidates):
        candidates_dic ["names"]= new_candidates[i]
        candidates_dic ["votes"]= candidates.count(new_candidates[i])
        candidates_dic ["percentage"] = str(round(candidates_dic ["votes"]*100/(len(total_voters)),2))
        print(f'{candidates_dic["names"]}: {candidates_dic["percentage"]}% ({candidates_dic["votes"]})')
    print("-------------------------")
    print("Winner:"+ candidates_dic["names"] + max(candidates_dic["percentage"])) 
    print("-------------------------")
    sys.stdout.close()