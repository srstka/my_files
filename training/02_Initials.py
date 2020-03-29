a = input("Hello! What is your full name?")
b = a.split(" ")

c = ""

for i in b:
    c += i[0]+"."
    
    
#print("Your initials are: ", b[0][0],b[1][0],b[2][0])

print("Your initials are: ", c)
