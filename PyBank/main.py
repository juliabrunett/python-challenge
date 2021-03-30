# Import csv and os module
import csv
import os

# Identify file for analysis
PyBank_file = os.path.join(".", "Resources", "budget_data.csv")
output_file = os.path.join(".", "analysis", "PyBankAnalysis.txt")

# Defining function for analyzing records
#def PyBank_Records(record):

# Open csv file
with open(PyBank_file, 'r') as csvfile:

    # Read csv file
    csv_read = csv.reader(csvfile, delimiter=',')
    
    # Take out title row in file
    csv_title = next(csv_read)

    total_amount = 0
    avg_change = 0
    greatest_increase = 0
    greatest_losses = 0
    increase_date = ""
    loss_date = ""

 # Define lists for dates, amounts & profit change by month
    dates = []
    amount = []
    profit_change_by_month = []

    # Loop through the file to create separate lists
    for row in csv_read:

    # append lists with each row's value
        dates.append(row[0])
        amount.append(row[1])

    # Find total months: length of 'dates' list    
    total_months = len(list(dates))

    # Loop through 'amount' list to find first and last values
    for _ in amount:

    # Find first and last amounts in list
        first_amount = int(amount[0])
        last_amount = int(amount[total_months - 1])

        # Calculate changes in Profit/Losses
        change = last_amount - first_amount

        # Find average of changes in Profit/Losses
        avg_change = change / (total_months - 1)
  
   # Find net total amount of Profit/Losses by looping through and adding each value
    for x in range(len(amount)):
        total_amount += int(amount[x])

    # Find profit change by month by looping through
    for index in range(len(amount)):

    # Set current month equal to current index
        current_month = int(amount[index])

    # Set previous month equal to previous index (set for next row)
        previous_month = int(amount[index - 1])

        # Add values to a new list to hold changes
        profit_change_by_month.append(current_month - previous_month)

        # Set current month equal to 0 (resetting for next row)
        current_month = 0

        # Find greatest increase in profits over period
        greatest_increase = max(profit_change_by_month)

        # Find greatest increase in losses over period
        greatest_losses = min(profit_change_by_month)

    for row in csv_read:
        if greatest_increase == row[1]:
            increase_date = row[0]
        if greatest_losses == row[1]:
            loss_date = row[0]    

        # Print findings
    print("FINCANCIAL ANALYSIS:")
    print("--------------------")
    print(f"Total Months: {total_months} months")
    print(f"Net Total Amount: ${total_amount}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {greatest_increase}")
    print(f"Greatest Increase in Losses: {greatest_losses}")
    
    print(f"Greatest Increase in Profits: {increase_date}, ${greatest_increase}")
    print(f"Greatest Increase in Losses: {loss_date}, ${greatest_losses}")
  

descriptions = ["Total Months", "Net Total Amount", "Average Change", "Greatest Increase in Profits", "Greatest Increase in Losses"]
output_values = [total_months, total_amount, avg_change, greatest_increase, greatest_losses]

clean_output = zip(descriptions, output_values)

  # Write to output file
with open(output_file, 'w', newline = '') as new_csv:

    # Write ouput to a file
    csv_write = csv.writer(new_csv, delimiter=',')

    csv_write.writerow(["Financial Analysis"])
    
    csv_write.writerows(clean_output)

    print("The results were saved into PyBankAnalysis.txt.")
        
