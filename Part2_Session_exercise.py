# TODO: Write a print statement that displays Different data type

x = ['a', 1, 18.2]
print(x[2])
print(x)
x.append("New_val")
print(x)
print(x[0])

# TODO: Write a print statement of dictionary is a data structure that stores simple key-value pairs

y = {"apples": 5, "pears": 2, "oranges": 9}
print(y["pears"])

# TODO: Write a print statement of Ordere dictionary Collection is a stores simple key-value 

from collections import OrderedDict
my_od = OrderedDict([('apples', 5), ('pears', 2), ('oranges', 9), ('bananas', 12)])

print (my_od["bananas"])

# TODO: Ierative Loops for Numaric, Charector Values
    
for xy in range (10):
    print(xy)

name_val = ["chris", "iftach", "jay"]
for Char in name_val:
    print(Char)


fruit_inventory = {"apples": 5, "pears": 2, "oranges": 9}
for fruit in fruit_inventory:
    print(fruit)

list(fruit_inventory.items())

for fruit in fruit_inventory.items():
    print (fruit)

for fruit, quantity in fruit_inventory.items():
    print("You have {} {}.".format(quantity, fruit))

# TODO: Conditional Loop and example infinite loop

xy = 0
while xy < 10:
    print(xy)
    xy += 2

from time import sleep
while True:
    try:
        print("Polling")
        sleep(1)
    except KeyboardInterrupt:
         break






