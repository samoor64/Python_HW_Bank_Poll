import os
import csv

#Set Path
csvpathh = os.path.join("Resources", "election_data.csv")

#Open CSV 
with open(csvpathh, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    total_votes = 0
    votes_khan = 0
    voter_correy = 0
    voter_li = 0
    voter_otooley = 0
    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            votes_khan += 1
        if row[2] == "Correy":
            voter_correy += 1
        if row[2] == "Li":
            voter_li += 1
        if row[2] == "O'Tooley":
            voter_otooley += 1
    winner = {"Khan": int(votes_khan), "Correy": int(voter_correy), "Li": int(voter_li), "OTooley": int(voter_otooley)}
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print("Khan: " + str(votes_khan) + str(int(votes_khan)/int(total_votes)))
    print("Correy: " + str(voter_correy) + str(int(voter_correy)/int(total_votes)))
    print("Li: " + str(voter_li) + str(int(voter_li)/int(total_votes)))
    print("O'Tooley: " + str(voter_otooley) + str(int(voter_otooley)/int(total_votes)))
    print("-------------------------")
    print("Winner: " + max(winner, key=winner.get))