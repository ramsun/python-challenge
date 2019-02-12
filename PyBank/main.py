'''
PyBank
main.py
Ramamurthy Sundar

This script showcases the csv library and its ability to read and analyze information
in a csv.  The summary results are posted to terminal and a text file.
'''
import csv

 # initialize key variables for analysis
mean = 0.0
greatest_val = 0
greatest_val_date = " "
lowest_val = 0
lowest_val_date = " "
total = 0
number_of_months = 0

path = "./budget_data.csv"
with open(path, newline ='') as casfileH:
    # assign the csv to a container
    csvContainer = csv.reader(casfileH, delimiter = ',')

    # loop through the csv container and perform analysis
    for aRow in csvContainer:
        # skip header row
        if aRow[0] == "Date":
            continue

        # increment number of months and running total
        number_of_months = number_of_months + 1
        total = int(aRow[1]) + total

        # assign value for temporary greatest profit 
        if int(aRow[1]) > greatest_val:
            greatest_val = int(aRow[1])
            greatest_val_date = aRow[0]
            
        # assign value for temporary biggest loss
        if int(aRow[1]) < lowest_val:
            lowest_val = int(aRow[1])
            lowest_val_date = aRow[0]
    
# calculate mean
mean = total / number_of_months

# print the results to the terminal and an output csv
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(number_of_months))
print("Total: " + str(total))
print("Average Change: " + "$" + str(round(mean,2)))
print("Greatest Increase in Profits: " + greatest_val_date + " ($" + str(greatest_val) + ")")
print("Greatest Decrease in Profits: " + lowest_val_date + " ($" + str(lowest_val) + ")")

# output to text file
output_file = open('financial_analysis.txt','w')
output_file.write('Financial Analysis' + "\n")
output_file.write("----------------------------"+ "\n")
output_file.write("Total Months: " + str(number_of_months)+ "\n")
output_file.write("Total: " + str(total)+ "\n")
output_file.write("Average Change: " + "$" + str(round(mean,2)) + "\n")
output_file.write("Greatest Increase in Profits: " + greatest_val_date + " ($" + str(greatest_val) + ")"+ "\n")
output_file.write("Greatest Decrease in Profits: " + lowest_val_date + " ($" + str(lowest_val) + ")")

# close file stream
output_file.close()
    