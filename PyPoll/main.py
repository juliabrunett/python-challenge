# Import os and csv modules
import os
import csv

# Identify file for analysis
PyPoll_file = os.path.join(".", "Resources", "election_data.csv")
# Identify file for output analysis
output_file = os.path.join(".", "analysis", "PyPollAnalysis.txt")

def percentage(num_votes, total_votes):

    percent = round((num_votes / total_votes) * 100, 2)

    return percent

# Open csv file
with open(PyPoll_file, 'r') as csvfile:

    # Read csv file
    csv_read = csv.reader(csvfile, delimiter=',')
    
    # Take out title row in file
    csv_title = next(csv_read)

    # Define lists for voterID, county, and candidates
    voterID = []
    county = []
    candidates = []

    # Initialize variables
    num_votes1 = num_votes2 = num_votes3 = num_votes4 = 0

    winner_name = ""
    candidate1 = "Khan"
    candidate2 = "Correy"
    candidate3 = "Li"
    candidate4 = "O'Tooley"
    
    # Loop through the file to create separate lists
    for row in csv_read:

        voterID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    # Find TOTAL VOTES: length of voterID list
    total_votes = len(list(voterID))

    # Count NUMBER OF VOTES for each candidate
    for index in range(len(candidates)):

        # Candidate 1
        if candidates[index] == candidate1:
            num_votes1 += 1

        # Candidate 2
        elif candidates[index] == candidate2:
            num_votes2 += 1

        # Candidate 3
        elif candidates[index] == candidate3:
            num_votes3 += 1

        # Candidate 4
        elif candidates[index] == candidate4:
            num_votes4 += 1


    # Find PERCENTAGE VOTES - pass through percentage function
    percent1 = percentage(num_votes1, total_votes)
    percent2 = percentage(num_votes2, total_votes)
    percent3 = percentage(num_votes3, total_votes)
    percent4 = percentage(num_votes4, total_votes)


    # Determine which CANDIDATE WON
    if percent1 > percent2 and percent1 > percent3 and percent1 > percent4:
        winner_name = candidate1
    elif percent2 > percent1 and percent2 > percent3 and percent2 > percent4:
        winner_name = candidate2
    elif percent3 > percent2 and percent3 > percent1 and percent3 > percent4:
        winner_name = candidate3
    elif percent4 > percent3 and percent4 > percent2 and percent4 > percent1:
        winner_name = candidate4
    

# OUTPUT RESULTS:
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")
    print(f"{candidate1}: {percent1}%, votes: {num_votes1}")
    print(f"{candidate2}: {percent2}%, votes: {num_votes2}")
    print(f"{candidate3}: {percent3}%, votes: {num_votes3}")
    print(f"{candidate4}: {percent4}%, votes: {num_votes4}")
    print("--------------------")
    print(f"Winner: {winner_name}")
    print("--------------------")

# Summary output descriptions
summary_desc = ["Total Votes", "Winning Candidate"]
# Summary output values
summary_values = [total_votes, winner_name]

# Define descriptions for output
descriptions = ["Khan", "Correy", "Li", "O'Tooley"]
# Define num output values
num_values = [num_votes1, num_votes2, num_votes3, num_votes4]
# Define percent output values
percent_values = [percent1, percent2, percent3, percent4]


# Zip output values & descriptions together
clean_output = zip(summary_desc, summary_values)
clean_output2 = zip(descriptions, percent_values, num_values)


  # Write to output file
with open(output_file, 'w', newline = '') as new_csv:

    # Write ouput to a file
    csv_write = csv.writer(new_csv, delimiter=',')

    # Write title row
    csv_write.writerow(["Summary Election Results:"])
    csv_write.writerow(["--------------------------"])
    
    # Write summary output rows
    csv_write.writerows(clean_output)

    # Write detailed title rows
    csv_write.writerow(["--------------------------"])
    csv_write.writerow(["--------------------------"])
    csv_write.writerow(["Detailed Election Results:"])
    csv_write.writerow(["--------------------------"])

    csv_write.writerow(["Candidate", " Percent of Votes", " Number of Votes"])
    csv_write.writerow(["-------------------------------------------"])

    # Write detailed output
    csv_write.writerows(clean_output2)

    # Notify user that results were output
    print("The results were saved into PyPollAnalysis.txt.")


