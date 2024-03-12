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


# %%