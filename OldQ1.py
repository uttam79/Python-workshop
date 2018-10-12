def sequence(z):
    a = []
    temp = []
    b = int(input("How many number you want to check ?: "))
    c = b
    
    while c != 0 :
        a.append(input("Enter number: "))
        c = c-1   
    temp = a
    for x in a:
        for y in temp:
            if x==y:
                z += 1
        return z           
        break
z = 0
result = sequence(z)
if result==1:
    print("all the numbers are different from each other")
else:
    print("some numbers in the sequence are repeating")