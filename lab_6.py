#%%
names_list = ['Jim', 'John', 'Marc']

for name in names_list:
    print(f"Hello {name}")

# %% 
for idx, name in enumerate(names_list):
    print(name)
    print(idx)

# %%
for i in range(0, 9):
    print(i)


# %%
name = "Arie"

for letter in name:
    print(letter)


# %% Assignment 1
'''
Create a loop that removes the vowels from the 
following names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] . 
Add the results to a new list.
'''

# initate the names list
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

# define the vowels
vowels = "aeouiy"


# initate an empty list
new_names_list = []

# iterate through each name
for name in names_list:

    # loop through all the letters
    for letter in name:
        if letter in vowels:
            name = name.replace(letter, "")
    
    print(name)
    new_names_list.append(name)





# %% Assignment 2
'''
Create a loop that prints the name of the day for the following 10 days
'''
import datetime
import locale


# set locale
locale.setlocale(locale.LC_ALL, 'nl_NL')


# define the date of today
today_date = datetime.date.today()

#%% define the number of days
num_days = 10

# %%
for days in range(1, num_days):
    # define the next date
    next_date = today_date + datetime.timedelta(days)

    # extract the name of the day
    day_name = next_date.strftime("%B, %A in het jaar %Y")

    # get the day name
    print(day_name)


    #print((today_date + datetime.timedelta(i)).strftime("%A"))
# %%
