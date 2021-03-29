# Import csv module
import csv

# Find file for analysis
csv_PyBank = "Resources/budget_data.csv"

# Defining function for analyzing records
def PyBank_Records(PyBank):

    # Define lists for dates, amounts & profit change by month
    dates = []
    amount = []
    profit_change_by_month = []

    # append lists with each row's value
    dates.append(PyBank[0])
    amount.append(PyBank[1])

    # Find net total amount of Profit/Losses
    total_amount = sum(amount)

    # Calculate changes in Profit/Losses
    if dates == "Jan-2010":
        first_amount = amount
    elif dates == "Feb-2017":
        last_amount = amount

    change = last_amount - first_amount

    # Find average of changes in Profit/Losses
    avg_change = change / (total_months - 1)
  
    # Profit change by month:
    # Set current month equal to current row amount
    current_month = amount

    # Set previous month equal to current month (set for next row)
    previous_month = current_month

    # Add values to a list
    profit_change_by_month.append(current_month - previous_month)

    # Set current month equal to 0 (resetting for next row)
    current_month = 0

    # Find greatest increase in profits over period
    greatest_increase = max(profit_change_by_month)

    # Find greatest increase in losses over period
    greatest_losses = min(profit_change_by_month)
  
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
    csv_read = csv.reader(csv_file, delimiter=',')
    
    # Take out title row in file
    csv_title = next(csv_read)

    total_months = len(list(csv_read))
    total_amount = 0

    # Loop through the file
    for row in csv_read:
        print(row)
        #PyBank_Records(row)

    print("ALL DONE!")
