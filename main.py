from datetime import datetime
from random import randint
import time


odds = []

for i in range(0, 60, 1):
  if i % 2 == 0:
    odds.append(i)

for i in range(0, randint(0, 21), 1):

    right_this_minute = datetime.today().minute
    
    if right_this_minute in odds:
        print("This minute seems a little odds")
    else:
        print("Not an odd minute")
    
    time.sleep(randint(0, randint(0, 31)))
print('This is END')