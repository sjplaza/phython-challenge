import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
net_total = 0

profit_loss = []
average_change = []
date = []

with open(budget_csv, 'r') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')
    header = next(budget_csv)
    file_to_output = "Analysis/budget_analysis.txt"

    for row in budget_csv:

        # The total number of months included in the dataset
        total_months = total_months + 1

# The net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(row[1])
        profit_loss.append(row[1])
        date.append(row[0])

# The average of the changes in "Profit/Losses" over the entire period
    for i in range(len(profit_loss) - 1):
        avg_period_change = int(profit_loss[i + 1]) - int(profit_loss[i])
        average_change.append(avg_period_change)

    change = abs(sum(average_change)/len(average_change))

# The greatest increase in profits (date and amount) over the entire period
    max_change = max(average_change)
    max_change_date = str(date[average_change.index(max(average_change))])

# The greatest decrease in losses (date and amount) over the entire period
    min_change = min(average_change)
    min_change_date = str(date[average_change.index(min(average_change))])

    print(f'')
    print(f'Financial Analysis')
    print(f'-----------------------')
    print(f'Total Months: ' + str(total_months))
    print(f'Total: ' + '$' + str(net_total))
    print(f'Average Change: ' + '$' + str(change))
    print(f'Greatest Increase in Profits: ' +
          str(max_change_date) + ' ($' + str(max_change) + ')')
    print(f'Greatest Decrease in Profits: ' +
          str(min_change_date) + ' ($' + str(min_change) + ')')

with open(file_to_output, 'w') as txt_file:
    txt_file.write('Total Months: ' + str(total_months))
    txt_file.write('\n')
    txt_file.write('Total: ' + '$' + str(net_total))
    txt_file.write('\n')
    txt_file.write('Average Change: ' + '$' + str(change))
    txt_file.write('\n')
    txt_file.write('Greatest Increase in Profits: ' +
                   str(max_change_date) + ' ($' + str(max_change) + ')')
    txt_file.write('\n')
    txt_file.write('Greatest Decrease in Profits: ' +
                   str(min_change_date) + ' ($' + str(min_change) + ')')
