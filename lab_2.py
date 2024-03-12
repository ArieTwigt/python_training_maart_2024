### Assignments

#%%
first_name = "Erling"
last_name  = "Haaland"

full_name  = first_name + last_name

full_name = "{} {}".format(first_name, last_name)

# %%
full_name


# %% Assignment 1
name = "Erling Haaland"

name = name + " .Jr"

print(name)
# %%
result = "{} {}".format(full_name, ".Jr")
result


# %% using an f-string
full_name_new = f"{full_name} .Jr"



# %% Replace the first name of Erling Haaland (Erling) to only the abbreviation of his first hame. This should result in: E. Haaland Jr.
full_name_new.replace("Erling", "E.")

# %%
full_name[0] + last_name

# %%
#full_name_new = "Arie Twigt"
full_name_list = full_name_new.split(" ")
# %%
first_letter = full_name_list[0][0]
full_name_list[0] = first_letter
full_name_list


#%%
full_name_new_abbrv = " ".join(full_name_list)




# %%
full_name_tuple = ('Erling', 'Haaland', '.Jr')

# %%
full_name_tuple[0] = first_letter


# %% Assignment 3: Create a variable called nationality with the value "Norway".
# Use this variable to create the string (sentence) "E. Haaland .Jr - Nationality: Norway". Print out the sentence.
nationality = "Norway"

# "E. Haaland .Jr - Nationality: Norway". 
sentence = f"{full_name_new_abbrv} - Nationality: {nationality}"
sentence 


# %%
