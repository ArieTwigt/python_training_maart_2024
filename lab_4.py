#%%
from datetime import date, timedelta, datetime


#%%
date.today()
# %%
datetime.now()
# %%
import os
# %%
os.mkdir("map")
# %%
os.listdir()

# %%
import time

time.tzname

# %%
datetime.now().astimezone().tzname()
# %%
from time import gmtime, strftime
print(strftime("%z", gmtime()))


### Assignments

# %% Assignment - Assign a variable that holds the number of days until your next birthday
from datetime import date

next_birthday = date(2024, 4, 1)

current_day = date.today()

diff_until_birthday = next_birthday - current_day

days_until_birthday = diff_until_birthday.days

f"Ik ben over {days_until_birthday} dagen jarig 🥳"


# %% Assignment 2
# Calculate the surface of a circle with a diameter of 10 (radius^ * pi)


import math


def calc_circle(diameter):
    radius = diameter / 2

    # calculate the size
    size = math.pow(radius, 2) * math.pi

    return size

calc_circle(50)


# %% Assignment 3: Create list that contains the files in your current working directory
import os

current_files_folders = os.listdir()
current_files_folders

# %% Assignment 4: Add a directory with the name our_functions
folder_name = "our_functions"

if folder_name not in current_files_folders:
    os.mkdir("our_functions")
else:
    print(f"{folder_name} alread exists")

# %%
