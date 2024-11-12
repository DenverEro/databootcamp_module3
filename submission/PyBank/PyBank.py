
# Dependencies
import csv
import os
from operator import itemgetter

# Files to load and output (update with correct file paths)
filepath = os.path.join("Resources/budget_data.csv")

# Define variables
total_months = 0
total_net = 0
last_month_profit = 0
current_month_profit = 0
total_change = 0
avg_change = 0
track_change = []

with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])

        # skip first row
        if total_months == 1:
            last_month_profit = int(row[1]) # Initialize with the first profit value
        else:
            # Get the current month profit and calculate change
            current_month_profit = int(row[1]) #B3, B4, B5...
            change = current_month_profit - last_month_profit  

            # Track the change with the date in a tuple (date, change)
            track_change.append((row[0], change))

            # Add to the total change
            total_change += change

            # Reset last month's profit to the current month for the next iteration
            last_month_profit = current_month_profit

    # Calculate the average change    
    avg_change = total_change / (total_months - 1)

# generate the output summary
output = (f"""Financial Analysis
          
----------------------------
          
Total Months: {total_months}

Total: ${total_net}

Average Change: ${avg_change}

Greatest Increase in Profits: {max(track_change, key = itemgetter(1))[0]} (${max(track_change, key = itemgetter(1))[1]})

Greatest Decrease in Profits: {min(track_change, key = itemgetter(1))[0]} (${min(track_change, key = itemgetter(1))[1]})
        """)

print(output)

# Write the results to a text file
results = "results.txt"
with open(results, "w") as txt_file:
    txt_file.write(output)