#%%
names_list = ['Arie', 'Zacherias','Jaap', 'Dirk', 'Jaap', 'Arie' ]
# %%
names_list.append('James')
# %%
names_list
# %%
names_list.remove("Arie")
# %%
names_list
# %%
names_list.remove("Dirk")
# %%
names_list
# %%

# %%
names_list
# %%
["Kanarie" if x == "Arie" else x for x in names_list ]


# %%
names_list = ['Arie', 'Dirk', 'Jaap']
# %%
# %%
if "James" in names_list:
   names_list.remove("James")
 
# %%


# %%
names_list + names_list
# %%
4 + "Arie"
# %%
"Arie" + 4

# %%
sorted(names_list)

#%%
names_list

#%%
names_list.sort()

#%%
names_list.sort(reverse=True)

# %%
x = list(set(names_list))
type(x)
x


# %%
person = {}

# %%
person['name'] = "James"
# %%
person
# %%
person['age'] = 26
# %%
person
# %%
person.keys()
# %%
person.values()
# %%
person['hobbies'] = ['mountainbike', 'football', 'reading']
# %%
person
# %%
person['pet'] = {'type': 'cat', 'age': 8}

# %%
person
# %%
person['pet']['age']
# %%
person.values()
# %%


### Assignments


#%% Assignment 1
person_1 = {"name": "Thijs", "age": 62, "hobbies": ['hiking', 'gardening', 'klussen']}


#%%
person_1





# %%
