# Import Modules

import os
import csv
import sys

# Create Lists to determine month and profit

total_month = []
total_profit = []

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
        average = float(total_month_amount / total_months)
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(total_month)))
    print("Total: $" + str(average))
    print("Average Change: $" + str(sum(total_profit)))
    print("Greatest Increase in Profits: " + (total_month[total_profit.index(max(total_profit))]) + " ($" +str(max(total_profit))+")")
    print("Greatest Decrease in Profits: " + (total_month[total_profit.index(min(total_profit))]) + " ($" +str(min(total_profit))+")")

    #Redirect Print to .txt

    sys.stdout=open("../analysis/main_output.txt","w")
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(total_month)))
    print("Total: $" + str(average))
    print("Average Change: $" + str(sum(total_profit)))
    print("Greatest Increase in Profits: " + (total_month[total_profit.index(max(total_profit))]) + " ($" +str(max(total_profit))+")")
    print("Greatest Decrease in Profits: " + (total_month[total_profit.index(min(total_profit))]) + " ($" +str(min(total_profit))+")")
    sys.stdout.close()

    