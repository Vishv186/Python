#TIME MODULE BASIC STRUCTURE(24hrs)

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)                                #https://doc.python.org/3/library/time.html#time.strftime
# timestamp = time.strftime('%H')                 #basic time module format
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# # timestamp = time.strftime('%S')
# # print(timestamp)

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)                                
timestamp1 = int(time.strftime('%H'))
print(timestamp1)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)

if(00 <= timestamp1 <= 12):
    print("Good Morning Sir")
elif(12 <= timestamp1 <= 18):
    print("Good Afternoon Sir")
elif(18 <= timestamp1 <= 24):
    print("Good Night Sir")




# #OTHER METHOD 

# import time
# t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))                   #Solution in video no.26 of code with harry.
# print(hour)

# if(hour>=0 and hour<12):
#     print("Good Morning Sir!")
# elif(hour>=12 and hour<17):
#     print("Good Afternoon Sir!")
# elif(hour>-17 and hour<0):
#     print("Good Night Str!")
