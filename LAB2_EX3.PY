# ParkingMeter.py
#
# author: A. N. Other
# date: September 2016

print("Kia Ora, this is a parking meter")

# set parking time
park_time = 4
print("park_time time is", park_time, "hours.")

# set rate and cost
rate = 4
cost = 0

# calculate parking cost
if park_time > 3:
    cost = rate * 3
    
    # drop the rate by $2
    rate -= 2
    
    # get the remaining parking time
    park_time -= 3
    
    # add remaining cost
    cost += rate * park_time
    
    print("The cost of the parking is $", cost)

else:
    cost = rate * park_time
    print("The cost of the parking is $", cost)

'''
Test Case
park_time = 4
Total cost of parking = $14
'''