first_name = input("Enter your first name") 
surname = input("Enter your surname") 
age = int(input("Enter your age"))
favourite_number =float(input("Enter your favourite number")) 
full_name =first_name + " " + surname

print(f"welcome, {full_name}!")
print(full_name.upper())
print(full_name.title())
print(f"Age in mounths: {age * 12}")
print(f"favourite number:{round(favourite_number, 2)}")

print(type(first_name))
print(type(surname))
print(type(age))
print(type(favourite_number))