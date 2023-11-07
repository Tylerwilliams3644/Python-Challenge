import os
import csv

path = os.path.join("election_data.csv")

political_candidates_dict = {}

political_candidates_names_list = []

political_candidates_names_set = set()

total_votes = 0

with open(path, "r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        Ballot_ID = row[0]
        County = row[1]
        candidate = row[2]
        if candidate not in political_candidates_names_list:
            political_candidates_names_list.append(candidate)
            political_candidates_dict[candidate] = 1
        else:
            political_candidates_dict[candidate] += 1
# Calculate and display the percentage of votes for each candidate
for candidate, votes in political_candidates_dict.items():
    percentage = (votes / total_votes) * 100
    political_candidates_dict[candidate] = {"votes": votes, "percentage": percentage}
# Find the winner
winner = max(
    political_candidates_dict, key=lambda x: political_candidates_dict[x]["votes"]
)
# Prepare the full text with line breaks
val = "\n\n".join(
    [
        f"{candidate}: {political_candidates_dict[candidate]['percentage']:.3f}% ({political_candidates_dict[candidate]['votes']})"
        for candidate in political_candidates_names_list
    ]
)
Full_Text = f"""
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
{val}
----------------------------
Winner: {winner}
----------------------------
"""
# Print the full text
print(Full_Text)
