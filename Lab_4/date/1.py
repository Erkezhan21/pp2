import datetime

now = datetime.datetime.now()
day = datetime.timedelta(5)
new_date = now - day

print(new_date.day)
