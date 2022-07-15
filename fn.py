import pandas as pd

while True:
    try:
        entries = int(input("How many entries would you like to submit?"))
        break
    except:
        print("This entry is invalid. Please enter an integer.")
    
counter = 0
while counter < entries:
    print(counter+ 1)
    counter += 1
    
    
#first_names = []
#last_names[]
#number_of_children = []

#for i in range(entries):
    