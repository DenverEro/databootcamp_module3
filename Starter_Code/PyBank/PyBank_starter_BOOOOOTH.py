# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

filepath = "Resources/budget_data.csv"

# Define variables to track the financial data
total_months = 0
total_net = 0

last_month_profit = 0
curr_month_profit = 0
total_change = 0

# Code ripped 3.2.8
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total_months += 1
        total_net += int(row[1])

        # check if first row - skip first row
        if total_months == 1:
            last_month_profit = int(row[1])
        else:
            # get change
            curr_month_profit = int(row[1])
            change = curr_month_profit - last_month_profit
            total_change += change

            # reset
            last_month_profit = curr_month_profit

# Generate the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${total_change / (total_months - 1)}
"""

# Print the output
print(output)
