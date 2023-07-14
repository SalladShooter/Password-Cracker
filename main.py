import random
from timeit import default_timer as timer

actualPassword = input("Password > ")

AIpassword = ""

start = timer()

# Solve Password
while True:
  if AIpassword == actualPassword:
    break
  AIpassword = ""
  
  for i in range(len(actualPassword)):
    AIpassword = AIpassword + chr(random.randint(33,126))

# Results
print(f"Password Has Been Cracked. Your Password Is: {AIpassword}")
end = timer()

# Time
total = end - start
if total >= 60:
  suffix = " Minutes"
elif total >= 3600:
  suffix = " Hours"
elif total >= 86400:
  suffix = " Days"
else:
  suffix = " Seconds"
print("It Took: " + str(round(total,5)) + suffix)
