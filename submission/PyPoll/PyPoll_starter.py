# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
filepath = os.path.join("Resources\election_data.csv")

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0.0

# Open the CSV file and process it
with open(filepath) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        # If the candidate is already in the dictionary, add a vote to the candidate's count
        else:
            candidate_votes[candidate] += 1

    # Collect candidate summaries
    candidate_summaries = []

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_votes.items():
        # Calculate the vote percentage
        vote_percentage = (votes / total_votes) * 100

        # Print the candidate's results to the terminal
        candidate_summary = (f"{candidate}: {vote_percentage:.3f}% ({votes} votes)")
        candidate_summaries.append(candidate_summary)

        # Determine if this candidate is the winning candidate
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

# Join all candidate summaries into a single string with line breaks
all_candidate_summaries = "\n".join(candidate_summaries)

# Generate and print the winning candidate summary
winning_summary = (f"""
-------------------------
Election Results
-------------------------
Total Votes: {total_votes}               
-------------------------
{all_candidate_summaries}
-------------------------
Winner: {winning_candidate}
-------------------------
""")
print(winning_summary)

# Save the winning candidate summary to the text file
results = "results.txt"
with open(results, "w") as txt_file:
    txt_file.write(winning_summary)