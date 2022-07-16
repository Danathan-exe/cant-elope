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

# counter for loop
counter = 1
while counter <= entries:
    _first_name = input("First name for entry " + str(counter) + ": ")
    _last_name = input("Last name for entry " + str(counter) + ": ")
    _number_of_children = input("Number of Children for entry " + str(counter) + ": ")
    first_names.append(_first_name)
    last_names.append(_last_name)
    number_of_children.append(_number_of_children)
    counter += 1
    

# the string
file_name_string = input("Input the Filename: ") + ".csv"

# create a pandas dataframe using lists from above
data_set = pd.DataFrame(
    {'firstName': first_names,
     'lastName': last_names,
     'children': number_of_children
    })

# write the pandas dataframe to a csv
data_set.to_csv(file_name_string)
