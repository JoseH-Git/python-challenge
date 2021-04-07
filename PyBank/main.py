# Import Modules

import os
import csv
import sys

# Create Lists to determine month and profit

total_month = []
total_profit = []
change = []

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Loop through lookin
    for row in csvreader:
        total_month.append(row[0])
        total_profit.append(int(row[1]))
        total_months = len(total_month)
        total_month_amount = sum(total_profit)
    

    for i in range(len(total_profit)-1):
        change.append(total_profit[i+1] - total_profit[i])
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(total_month)))
    print("Total: $" + str(sum(total_profit)))
    print("Average Change: $" + str(round(sum(change)/len(change),2)))
    print("Greatest Increase in Profits: " + (total_month[change.index(max(change))+1]) + " ($" +str(max(change))+")")
    print("Greatest Increase in Profits: " + (total_month[change.index(min(change))+1]) + " ($" +str(min(change))+")")

    #Redirect Print to .txt

    sys.stdout=open("../analysis/main_output.txt","w")
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(total_month)))
    print("Total: $" + str(sum(total_profit)))
    print("Average Change: $" + str(round(sum(change)/len(change),2)))
    print("Greatest Increase in Profits: " + (total_month[change.index(max(change))+1]) + " ($" +str(max(change))+")")
    print("Greatest Increase in Profits: " + (total_month[change.index(min(change))+1]) + " ($" +str(min(change))+")")
    sys.stdout.close()