person = {"name":"John", "gender":"fluent","age":"34","address":"New York","phone":12345}
inf = input("What information about the user do you want to get? (name,gender,age,address,phone): " ).lower()
print(person.get(inf,"I could not find the requested information"))
