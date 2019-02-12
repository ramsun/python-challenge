'''
PyBoss
main.py
Ramamurthy Sundar

This script uses the csv library in order to both read
and write a file.  Information such as the full name, date
of birth, SSN, and State from employee_data1.csv are transformed
according to the spec, which states that:
1. Names of employees must by split (first and last name)
2. DOB must be in the format month/date/year
3. Bleep out the first 5 numbers of their SSN
4. Abbreviate their birth state
This information is exported to a csv.
'''
import csv

# dictionary of US states and their abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# initialize variables
infile_path = "./employee_data.csv"
outfile_path = "./employee_data2.csv"
SSN_bleeped = ""
Date_rearranged = ""
year = ""
month = ""
date = ""

# open output file stream
with open(outfile_path, mode='w', newline = '') as employee_file:
    # create a csv writer object
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # initialize the first row of employee_data2.csv
    employee_writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # open input file stream
    with open(infile_path, newline ='') as casfileH:
        # create a csv reader object
        csvContainer = csv.reader(casfileH, delimiter = ',')
        
        # go through the csv reader object and 
        for aRow in csvContainer:
            # skip header row
            if aRow[0] == "Emp ID":
                continue

            # split the name column from csv 1
            first_name, last_name = aRow[1].split()

            # Create a string of the new 
            for idx, val in enumerate(aRow[2]):
                # assign year
                if idx < 4:
                    year += val
                # the char is a dash (do nothing)
                elif val == '-':
                    continue
                # assign month
                elif idx > 4 and idx < 7:
                    month += val
                # assign date
                else:
                    date += val
            Date_rearranged = month + '/' + date + '/' + year

            #bleep out the SSN
            for idx, val in enumerate(aRow[3]):
                # the SSN charachters after the first 5 do not need to be bleeped
                if idx > 5:
                    SSN_bleeped = SSN_bleeped + val
                # the charachter is a dash, do not bleep it out
                elif val == '-':
                    SSN_bleeped = SSN_bleeped + val
                # bleep the charachter
                else:
                    SSN_bleeped = SSN_bleeped + '*'

            # shorten state to abbreviation
            state_abv = us_state_abbrev[aRow[4]]

            # write all of the variables to employee_data2.csv
            employee_writer.writerow([aRow[0], first_name, last_name, Date_rearranged, SSN_bleeped, state_abv])

            # clear all the of string variables for the next row of employees
            first_name = ''
            last_name = ''
            year = ''
            month = ''
            date = ''
            Date_rearranged = ''
            SSN_bleeped = ''
            state_abv = ''
            


        



