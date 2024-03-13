


### Assignments

#%% Assignment 1: Create a conditional statement that indicates if your name starts with an "A or not
name = "Arie"

if name[0].lower() == "a":
    print("Your name starts with an 'A'")
else:
    print("Your name does not start with an 'A'")


#%% Assignment 2:
    
'''
Create a conditional statement that indicates if your name begins with a vowel. If it does, change it into a non-vowel and otherwise. 
For example: Arie –> Brie or Rose –> Aose
'''

# define the vowels
vowels = "aeoui"

name = "Dirk"

if name[0].lower() in vowels:
    new_name = name.replace(name[0], "B")
    print(new_name)
else:
    new_name = name.replace(name[0], "A")
    print(new_name)



# %% Assignment 3a:Create a conditional statement that indicates if your age is between 18 and 68

age = 34

if age > 18 and age < 68:
    print("Ja")


#%% 3b
age = 34

if 18 < age < 68:
    print("Ja")






# %%
