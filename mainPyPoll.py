import os
import csv

# Define the file path for the election data
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables to store election data
total_votes = 0
candidate_votes = {}

# Open and read the CSV file
try:
    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)  # Skip the header row
        
        # Process each row in the dataset
        for row in csvreader:
            total_votes += 1  # Count total votes
            
            candidate = row[2]  # Candidate name is in the third column
            
            # Count the votes for each candidate
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

except FileNotFoundError:
    print("The file was not found. Please check the file path and try again.")
    exit()  # Exit the script if the file is not found

# Proceed with calculations if the file was found
if total_votes > 0:
    # Determine the winner and calculate vote percentages
    winner = ""
    winner_votes = 0

    # Prepare to write the results to a text file
    with open('analysis/results.txt', 'w') as txtfile:
        # Write header to the text file
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")
        
        # Display election results
        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {total_votes}")
        print("-------------------------")
        
        for candidate, votes in candidate_votes.items():
            vote_percentage = (votes / total_votes) * 100
            
            # Write each candidate's result to the text file
            txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
            
            # Print each candidate's result
            print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
            
            # Determine the winner based on popular vote
            if votes > winner_votes:
                winner_votes = votes
                winner = candidate

        # Write the winner to the text file
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("-------------------------\n")
        
        # Print the winner of the election
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

else:
    print("No votes found in the dataset.")
