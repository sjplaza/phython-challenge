import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

total_votes = 0

# A complete list of candidates who received votes
candidates = []

# The total number of votes each candidate won
num_votes = []

# The percentage of votes each candidate won
percent_votes = []

with open(election_csv, 'r') as csvfile:
    election_csv = csv.reader(csvfile, delimiter=',')
    header = next(election_csv)
    file_to_output = "Analysis/election_analysis.txt"

    for row in election_csv:

        # The total number of votes cast
        total_votes = total_votes + 1

# Find the candidate and count their vote
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

# Add the percentage of votes for each candidate
    for votes in num_votes:
        percentage = (votes / total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

# The winner of the election based on popular vote.
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_cand = candidates[index]

    print(f'')
    print(f'Election Results')
    print(f'-----------------------')
    print(f'Total Votes: {str(total_votes)}')
    print(f'-----------------------')
    for i in range(len(candidates)):
        print(f'{candidates[i]}: {str(percent_votes[i])}  {str(num_votes[i])}')
    print(f'-----------------------')
    print(f'Winner: {winning_cand}')
    print(f'-----------------------')

with open(file_to_output, 'w') as txt_file:
    txt_file.write('Election Results')
    txt_file.write('\n')
    txt_file.write(str(f'Total Votes: {str(total_votes)}'))
    txt_file.write('\n')
    for i in range(len(candidates)):
        txt_file.write(
            str(f'{candidates[i]}: {str(percent_votes[i])}  {str(num_votes[i])}'))
        txt_file.write('\n')
    txt_file.write(str(f'Winner: {winning_cand}'))
