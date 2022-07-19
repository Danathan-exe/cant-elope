import os.path
import pandas as pd

print("""
This program takes entries of first name, last name, and number 
of children. You will first select how many entries you would like
to enter, then you will input the data for each entry. Finally, you
will chose the filename for the .csv export.
""")

# exception handling to assure only an int or float is inputted
while True:
    try:
        entries = int(input("How many entries would you like to submit?"))
        # if a float is inputted, it will be automatically rounded down to the next int
        break
    except:
        print("This entry is invalid. Please enter an integer.")   

# make lists
first_names = []
last_names = []
number_of_children = []
hours_per_week = []

# counter for loop
counter = 1
while counter <= entries:
    _first_name = input("First name for entry " + str(counter) + ": ")
    _last_name = input("Last name for entry " + str(counter) + ": ")
    _number_of_children = input("Number of Children for entry " + str(counter) + ": ")
    _hours_per_week = input(" how many hours do you work?" + str(counter) + ":  ")
    first_names.append(_first_name)
    last_names.append(_last_name)
    number_of_children.append(_number_of_children)
    hours_per_week.append(_hours_per_week)
    counter += 1

# the string
file_name_string = input("Input the Filename: ") + ".csv"

#checking file name
file_exists = os.path.exists(file_name_string)
print(file_exists)
filesafe = input("are you sure you want to name the file that?  y/N")

if filesafe == "y":

# create a pandas dataframe using lists from above
    data_set = pd.DataFrame(
        {'firstName': first_names,
        'lastName': last_names,
        'children': number_of_children
        'hours': hours_per_week
    })

    # write the pandas dataframe to a csv
    data_set.to_csv(file_name_string)

else:
    break

