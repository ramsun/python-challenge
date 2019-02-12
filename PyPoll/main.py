# PyPoll
# Ramamurthy Sundar
import csv

# initialize variables that will be used in report
election_dict = {} # key = candidate name : value = votes of candidate
total = 0

# open the csv
path = "./election_data.csv"
with open(path, newline ='') as casfileH:
    # assign the csv to a container
    csvContainer = csv.reader(casfileH, delimiter = ',')
    
    # loop through the csvContainer
    for aRow in csvContainer:
        # skip header row
        if(aRow[0] == "Voter ID"):
            continue
            
        # update total value
        total = total + int(aRow[0])

        # assign the row to the election dictionary
        if aRow[2] in election_dict:
            election_dict[aRow[2]] += int(aRow[0])
        else:
            election_dict[aRow[2]] = int(aRow[0])

#print the results to terminal and text file
outfile = open("election_results.txt", 'w')
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total))
print("-------------------------")
outfile.write("Election Results" + "\n")
outfile.write("-------------------------" + "\n")
outfile.write("Total Votes: " + str(total) + "\n")
outfile.write("-------------------------" + "\n")

# go through each key in the dictionary
for aKey in election_dict:
    print(aKey + ": " + str(round((election_dict[aKey] / total) * 100,3)) + "% (" + str(election_dict[aKey]) + ")")
    outfile.write(aKey + ": " + str(round((election_dict[aKey] / total) * 100,3)) + "% (" + str(election_dict[aKey]) + ")" + "\n")

# print the winner
print("-------------------------")
print("Winner: " + max(election_dict, key=election_dict.get))
print("-------------------------")
outfile.write("-------------------------" + "\n")
outfile.write("Winner: " + max(election_dict, key=election_dict.get) + "\n")
outfile.write("-------------------------" + "\n")

# close 
outfile.close()


        
