import os
import csv

date_count = 0
budget_total = 0
max_value = 0
min_value = 0
average_total = 0
previous_value = 0
new_value = 0
row_loop = 1

#path to get data from budget_data.csv and outputting it to a text file
budget_data = os.path.join('..', 'PyBank', 'budget_data.csv') 
output_text = os.path.join("PyBank.txt")

#reader for budget_data.csv
with  open(budget_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
 
    #loop through rows in budget_data.csv, skipping the header   
    for row in csv_reader:
        
        #grabs first budget, does not add to running average change total
        if row_loop == 1:
            row_loop =2
            previous_value = int(row[1])
            date_count = date_count + 1
            
            #running total for budget
            budget_total = budget_total + int(row[1])
            
            
            #if statements collecting max/min values of budgets
            if int(row[1]) > max_value:
                max_value = int(row[1])
                max_date = row[0]
                
            if int(row[1]) < min_value:
                min_value = int(row[1])
                min_date = row[0]
                
        else:
            
            #counter for total months and final average 
            date_count = date_count + 1
            new_value = int(row[1])
            average_total = average_total + new_value - previous_value
            previous_value = new_value
            
            #running total for budget
            budget_total = budget_total + int(row[1])
            
            #if statements collecting max/min values of budgets
            if int(row[1]) > max_value:
                max_value = int(row[1])
                max_date = row[0]
            
            if int(row[1]) < min_value:
                min_value = int(row[1])
                min_date = row[0]


#counters a case where a number is divided by 0                
if date_count == 0:
    average = 0
else:
    average = average_total / (date_count - 1)

#print answers to shell
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {str(date_count)}")
print(f"Total: {str('${}'.format(budget_total))}")
print(f"Average Change:  {str('${:.2f}'.format(average))}")
print(f"Greatest Increase in Profits: {str(max_date)} ({str('${}'.format(max_value))})")
print(f"Greatest Decrease in Profits: {str(min_date)} ({str('${}'.format(min_value))})")

#open text file PyBank
file = open(output_text, "w")

#write answers to a text file
file.write("Financial Analysis\n")
file.write("-----------------------------------\n")
file.write(f"Total Months: {str(date_count)}" + "\n")
file.write(f"Total: {str('${}'.format(budget_total))}" + "\n")
file.write(f"Average Change:  {str('${:.2f}'.format(average))}" + "\n")
file.write(f"Greatest Increase in Profits: {str(max_date)} ({str('${}'.format(max_value))})" + "\n")
file.write(f"Greatest Decrease in Profits: {str(min_date)} ({str('${}'.format(min_value))})" + "\n")

file.close()