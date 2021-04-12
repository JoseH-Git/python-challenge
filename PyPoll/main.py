# Import Modules

import os
import csv
import sys

# Create Lists to determine total voters and candidates

total_voters = []
candidates = []
winner = []
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
    candidates_dic = {"names": [] , "votes": [], "percentage": []}

    print("Election Results")
    print("-------------------------")
    print("Total Voters: " + str(len(total_voters)))
    print("-------------------------")
    for i in range(total_candidates):
        candidates_dic ["names"].append(new_candidates[i])
        candidates_dic ["votes"].append(candidates.count(new_candidates[i]))
        candidates_dic ["percentage"].append(str(round(candidates_dic["votes"][i]*100/(len(total_voters)),2)))
        print(f'{candidates_dic["names"][i]}: {candidates_dic["percentage"][i]}% ({candidates_dic["votes"][i]})')
    print("-------------------------")
    for i in range(total_candidates):
        if float(candidates_dic["percentage"][i]) == float(max(candidates_dic["percentage"])):
                print("Winner: " + candidates_dic["names"][i])
    print("-------------------------")

    #Redirect Print to .txt
    
    sys.stdout=open("../analysis/main_output.txt","w")
    print("Election Results")
    print("-------------------------")
    print("Total Voters: " + str(len(total_voters)))
    print("-------------------------")
    for i in range(total_candidates):
        candidates_dic ["names"].append(new_candidates[i])
        candidates_dic ["votes"].append(candidates.count(new_candidates[i]))
        candidates_dic ["percentage"].append(str(round(candidates_dic["votes"][i]*100/(len(total_voters)),2)))
        print(f'{candidates_dic["names"][i]}: {candidates_dic["percentage"][i]}% ({candidates_dic["votes"][i]})')
    print("-------------------------")
    for i in range(total_candidates):
        if float(candidates_dic["percentage"][i]) == float(max(candidates_dic["percentage"])):
                print("Winner: " + candidates_dic["names"][i])
    print("-------------------------")
    sys.stdout.close()