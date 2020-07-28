import os
import csv
total_months = 0
net_total = 0

budget_csv = os.path.join('Resources', 'budget_data.csv')


def acctg_data(budget_data):
    date = str(budget_data[0])
    total = int(budget_data[1])


with open(budget_csv) as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget_csv)
    print(f'CSV Header: {csv_header}')

# The total number of months included in the dataset
    for row in budget_csv:
        total_months = total_months + 1

# The net total amount of "Profit/Losses" over the entire period
    for col in budget_csv:
        net_total = sum(budget_data[1])

# The average of the changes in "Profit/Losses" over the entire period


# The greatest increase in profits(date and amount) over the entire period


# The greatest decrease in losses(date and amount) over the entire period

print(f'')
print(f'Financial Analysis')
print(f'------------------------')
print(f'Total months: {total_months}')
print(f'Net total: {net_total}')
