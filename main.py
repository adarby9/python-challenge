import csv
import os
datafile=os.path.join("Resources","election_data.csv")
with open(datafile) as file:
    reader = csv.reader(file)
    next(reader)
    data = list(reader)

    total_votes = len(data)  

candidate_votes = {}

for row in data:
    candidate = row[2]

    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

winner_votes = 0
winner = ""

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")