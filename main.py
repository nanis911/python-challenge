#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period

import os
import csv

# Define the file path
csvpath = os.path.join('/Users/nathalylamas/Downloads/python-challenge/PyBank/Resources/budget_data.csv')

# Print the path to check correctness
print(f"CSV Path: {csvpath}")

# Initialize lists to store data
dates = []
profit_losses = []

# Open and read the CSV file
try:
    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)  # Skip the header row
        
        for row in csvreader:
            dates.append(row[0])  # Date column
            profit_losses.append(int(row[1]))  # Profit/Losses column

except FileNotFoundError:
    print("The file was not found. Please check the file path and try again.")
    exit()  # Exit the script if the file is not found

# Proceed with calculations if the file was found
if dates and profit_losses:
    # Calculate the total number of months
    total_months = len(dates)

    # Calculate the net total amount of "Profit/Losses"
    net_total = sum(profit_losses)

    ##The changes in "Profit/Losses" over the entire period, and then the average of those changes
    changes = []
    for i in range(1, len(profit_losses)):
        change = profit_losses[i] - profit_losses[i - 1]
        changes.append(change)

    if len(changes) > 0:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0

    #The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
    greatest_increase_date = ''
    greatest_increase_amount = float('-inf')
    greatest_decrease_date = ''
    greatest_decrease_amount = float('inf')

    for i in range(len(changes)):
        if changes[i] > greatest_increase_amount:
            greatest_increase_amount = changes[i]
            greatest_increase_date = dates[i + 1]  # Date corresponding to the change
        if changes[i] < greatest_decrease_amount:
            greatest_decrease_amount = changes[i]
            greatest_decrease_date = dates[i + 1]  # Date corresponding to the change

    # Display the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total:,.0f}")
    print(f"Average Change: ${average_change:,.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount:,.0f})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount:,.0f})")


