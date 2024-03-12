#%%
from datetime import datetime, timezone

#%% local time with timezone information
local_time = datetime.now().astimezone()

#%% local timezone
local_timezone = local_time.tzinfo

#%% current time in UTC
utc_time = datetime.now(timezone.utc)

#%% differences
time_difference_seconds = local_time.utcoffset().total_seconds()
time_difference_hours = time_difference_seconds / 3600

#%%
print(f"Local timezone: {local_timezone}")
print(f"Current local time: {local_time}")
print(f"Time difference with UTC (in hours): {time_difference_hours}")