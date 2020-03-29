birthday = input("Please insert your birthday in the format DD-MM-YYYY: ")

months=("January","Februari","March","April","May","June","July","August","September","October","November","December")

#print("You have been born in:", months[(int(birthday.split("-")[1])-1)])

print("You have been born in:", months[(int(birthday[3:5])-1)])
