# Import csv and os modules
import csv
import os

# Identify file for analysis
PyBank_file = os.path.join(".", "Resources", "budget_data.csv")
# Identify file for output
output_file = os.path.join(".", "analysis", "PyBankAnalysis.txt")

# OPEN CSV FILE
with open(PyBank_file, 'r') as csvfile:

    # READ CSV FILE
    csv_read = csv.reader(csvfile, delimiter=',')
    
    # Take out title row in file
    csv_title = next(csv_read)

    # Initialize variables
    total_amount = 0
    avg_change = 0
    greatest_increase = 0
    greatest_losses = 0
    increase_date = ""
    loss_date = ""

    # Create & define lists for dates, amounts & profit change by month
    dates = []
    amount = []
    profit_change_by_month = []


    # Loop through the file to create separate lists
    for row in csv_read:

    # Append lists with each row's value
        dates.append(row[0])
        amount.append(row[1])

    # Find TOTAL MONTHS: length of 'dates' list (without title row)  
    total_months = len(list(dates))


    # Loop through 'amount' list to find first and last values & add value to total amount
    for x in range(len(amount)):
    
    # Find NET TOTAL AMOUNT of Profit/Losses by looping through and adding each value
        total_amount += int(amount[x])

    # Find first and last monthly amounts in 'amount' list
        first_amount = int(amount[0])
        last_amount = int(amount[total_months - 1])

        # Calculate changes in Profit/Losses
        change = last_amount - first_amount

        # Find AVERAGE OF CHANGES in Profit/Losses
        avg_change = change / (total_months - 1)

        # Round average change to 2 decimal places
        rounded_avg_change = round(avg_change, 2)

    # Find profit change by month by looping through 'amount' list
        # Set current month equal to current index
        current_month = int(amount[x])

        # Set previous month equal to previous index (set for next row)
        previous_month = int(amount[x - 1])

        # Add values to a new 'profit change' list to hold monthly changes
        profit_change_by_month.append(current_month - previous_month)

        # Set current month equal to 0 (resetting for next row)
        current_month = 0

    # Find GREATEST INCREASE IN PROFITS over period
    greatest_increase = max(profit_change_by_month)

    # Find GREATEST INCREASE IN LOSSES over period
    greatest_losses = min(profit_change_by_month)


    # Loop through 'profit change' list to find indexes of values
    for index in range(len(profit_change_by_month)):

        # Find profit index
        if greatest_increase == profit_change_by_month[index]:
            profit_index = index

        # Find losses index
        if greatest_losses == profit_change_by_month[index]:
            loss_index = index
    
    # Find DATES that correspond with the profit/loss values (from 'dates' list)
    profit_date = dates[profit_index]
    loss_date = dates[loss_index]


# OUTPUT RESULTS

     # Print findings for user in terminal
    print("FINCANCIAL ANALYSIS:")
    print("--------------------")
    print(f"Total Months: {total_months} months")
    print(f"Net Total Amount: ${total_amount}")
    print(f"Average Change: ${rounded_avg_change}")
    print(f"Greatest Increase in Profits: {profit_date}, ${greatest_increase}")
    print(f"Greatest Increase in Losses: {loss_date}, ${greatest_losses}")
  
# Define descriptions for output
descriptions = ["Total Months", "Net Total Amount", "Average Change", "Greatest Increase in Profits", "Profit Date", "Greatest Increase in Losses", "Loss Date"]
# Define output values
output_values = [total_months, total_amount, rounded_avg_change, greatest_increase, profit_date, greatest_losses, loss_date]

# Zip output values & descriptions together
clean_output = zip(descriptions, output_values)

  # Write to output file
with open(output_file, 'w', newline = '') as new_csv:

    # Write ouput to a file
    csv_write = csv.writer(new_csv, delimiter=',')

    # Write title row
    csv_write.writerow(["Financial Analysis"])
    
    # Write all output rows
    csv_write.writerows(clean_output)

    # Notify user that results were output
    print("The results were saved into PyBankAnalysis.txt.")
        
