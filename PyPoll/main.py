#the following code iterates over a dataset of voters and returns the winner candidate

import os
import csv

csv_path = os.path.join("resources", "election_data.csv")

#======================================================
#this block code looks for rows with a different format than expected

# index = 0
# 
# with open(csv_path) as votes_data:
#     reader = csv.reader(votes_data, delimiter = ",")
#     next(reader) #skip the very first row of the file
#     header = next(reader) #skip the header
#     for row in reader:
#         #identify rows with different formats than 'Id,County,Candidate'
#         if len(row) < 3 or row == header:
#             print(row) #visualize the row
#             print(index) #identify row index
#         index += 1

#based on the results of the previous code block, you discover a '======' row and a second
#header after that. This block compares the first log of the first table and the first log
#of the second table to demonstrate they're the same ID. Thus, the dataset is duplicated.

#with open(csv_path) as votes_data:
    #reader = csv.reader(votes_data, delimiter = ",")
    #next(reader) #skip the very first row of the file
    #header = next(reader) #skip the header
    #first_voter = [row for index, row in enumerate(reader) if index == 0 or index == 3521003]
    #print(first_voter)

#=====================================================

votes_count = 0
candidates = {}
with open(csv_path) as votes_data:
    reader = csv.reader(votes_data, delimiter = ",")
    next(reader)
    next(reader)
    for row in reader:
        if len(row) < 3: #stop 'for loop' when reaching the '======' row
            break
        else:
            votes_count += 1 #total votes for the entire election
            if not(row[2] in candidates):
                 candidates[row[2]] = {"votes" : 1} #add candidate name to 'candidates' dict 
            else:
                 candidates[row[2]]["votes"] += 1 #add subsequent votes


#iterate over the votes gathered by each candidate to calculate percentage of votes
for candidate, info in candidates.items():
    percentage = info["votes"] / votes_count
    info["percentage"] = format(round(percentage, 2), "%")

#gather the votes of each candidate to get the maximum value
votes = []
for candidate, info in candidates.items():
    votes.append(info["votes"])
max_votes = max(votes)

#match the maximum value of votes with the candidate name
winner = [key for key, value in candidates.items() if value["votes"] == max_votes]

#iteration to build the candidates results chart
chart= ""
for candidate, info in candidates.items():
    chart += "{}: {}% ({})\n".format(candidate, (info["percentage"])[:-4], info["votes"])

#build the final output
election_results =\
    "\nElection Results\n\
----------------------------\n\
Total Votes: {}\n\
----------------------------\n\
{}----------------------------\n\
Winner : {}\n\
----------------------------".format(votes_count, chart, winner[0])
print(election_results)

#create the report with the election results
with open(os.path.join("analysis", "election_results.txt"), "w") as results:
    results.write(election_results)