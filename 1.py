# TODO: Print Current Date and Time
import datetime

cudt = datetime.datetime.now()

print ("Current Date & Time :- ",cudt)

# TODO: Print Even numbers

def even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print("Even Numbers :- ", even_num([243, 333,45, 234,788, 345, 66, 74,492, 371]))