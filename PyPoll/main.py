import os
import csv

total_votes = 0

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    poll_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(poll_data)
    print(f"CSV Header: {csv_header}")

# The total number of votes cast
    for row in poll_data:
        total_votes = total_votes + 1

# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.


print(f'')
print(f'Election Results')
print(f'---------------------')
print(f'Total Votes: {total_votes}')
print(f'---------------------')
