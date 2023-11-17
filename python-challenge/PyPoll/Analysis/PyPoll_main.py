# PyPoll

# Import modules

import os
import csv

# Connect path to folder

PyPollcsv = os.path.join("Resources","election_data.csv")

# Create lists to store data

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open CSV using set path PyPollcsv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #Skip the header row
    
    #Iterate through each row in the CSV file    
    for row in csvreader:
        # Count total votes
        total_votes += 1
        # Extract the candidate name from the row
        candidate_name = row[2]
        
        # Update the candidate's vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1    
    
# Print election results 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes : {total_votes}")    
print("-------------------------")

# Iterate through the candidates and print their results
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Update the winner information if needed
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Print to a text file: election_results.txt
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f"Total Votes : {total_votes}\n")
    text.write("---------------------------------------\n")
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        text.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    text.write("---------------------------------------\n")
    text.write(f"The winner is: {winner}\n")
    text.write("---------------------------------------\n")


