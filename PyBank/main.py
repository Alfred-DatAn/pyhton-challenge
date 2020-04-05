#the current code analyzes the financial records of a company in a given period

import os
import csv

#path to the dataset
csv_path = os.path.join("resources", "budget_data.csv")


month_count = [] #list to store unique month values
net_total = 0 #variable to sum the profit or losses of each month
profit_loss = 0 #variable to store the previous profit/loss value to calculate the change with the following month
revenue_change = [] #list to store the revenue change of each month

with open (csv_path) as csv_file:
    reader = csv.reader(csv_file, delimiter = ",")
    next(reader) #skip the very first row of the file '<<<<<<< HEAD'
    next(reader) #skip the header for the 'for loop'
    for row in reader:
        if len(row) < 2: #prevent the 'for loop' of continuing after reaching a row with different format
            break
        else:
            if not(row[0] in month_count): #evaluates the current month with the list 'month_count'
                month_count.append(row[0]) #add the month in 'month_count'
                net_total += int(row[1]) #sum the profit_loss value
            revenue_change.append(int(row[1])-profit_loss)#calculates the revenue change between months
            profit_loss = int(row[1]) #set the new value for the next revenue_change computation
            
#since first value of the 'revenue_change' list is only the profit of the first month, I ignore it
#for the average change computation
average_revenue = round(sum(revenue_change[1:]) / (len(revenue_change) -1), 2)

#find the highest and lowest values in the revenue_change list
great_increase, great_decrease = max(revenue_change), min(revenue_change)
#get the index of thosethe previous values to access to the same values in the 'month_count' list as well
index_in = revenue_change.index(great_increase)
index_de = revenue_change.index(great_decrease)

#build the final report
final_report =\
    "\nFinancial Analysis\n\
-------------------------\n\
  Total months: {}\n\
  Total: ${}\n\
  Average change: ${}\n\
  Greatest increse in profits: {} (${})\n\
  Greatest decrease in profits: {} (${})"\
.format(len(month_count), net_total, average_revenue, month_count[index_in],\
great_increase,month_count[index_de], great_decrease)

#print it
print(final_report)

#create a txt file with the results
with open(os.path.join("analysis", "pybank_report.txt"), "w") as report:
       report.write(final_report)