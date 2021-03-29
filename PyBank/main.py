# Import csv module
import csv

# Find file for analysis
csv_PyBank = "../Resources/budget_data.csv"

# Defining function for analyzing records
def PyBank_Records(PyBank):

    dates = int(PyBank[0])
    amount = int(PyBank[1])

    # Find total number of months
    total_months = 

    # Find net total amount of Profit/Losses
    total_amount = (sum(amount))

    # Calculate changes in Profit/Losses
    change = 

    # Find average of changes in Profit/Losses
    avg_change = 

    # Find greatest increase in profits over period
    greatest_increase = 

    # Find greatest increase in losses over period
    greatest_losses = 

# Print findings
    print("FINCANCIAL ANALYSIS:")
    print("--------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_amount}")
    print(f"Average Change: {avg_change}")
    print(f"Greatest Increase in Profits: {dates}, {greatest_increase}")
    print(f"Greatest Increase in Losses: {dates}, {greatest_losses}")

# Open csv file
with open(csv_PyBank, 'r') as csv_file:

    # Read csv file
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Take out header
    csv_header = next(csv_reader)

    # Loop through the file
    for row in csv_reader:
        PyBank_Records(row)
        