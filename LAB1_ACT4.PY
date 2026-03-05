from datetime import datetime

# now() method is used to get current date and time
now_method = datetime.now()

# strftime() method is used to format date and time
currentTime = now_method.strftime("%d-%m-%Y %H:%M:%S")

print("Current Date and Time =", currentTime)