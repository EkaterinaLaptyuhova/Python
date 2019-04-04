# Exercise 5-1
import time


current_time = time.time()
print(current_time)
days = int(current_time // 86400)
years = int(days // 365)
sec_current_day = int(current_time % 86400)
hours = int(sec_current_day // 3600)
min = (sec_current_day - int(hours * 3600)) // 60
sec = int(sec_current_day - ((sec_current_day - int(hours * 3600)) // 60) * 60 - int(hours * 3600))
print(hours, ":", min, ".", sec)




