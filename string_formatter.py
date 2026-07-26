# Collect user information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio ")

# Create username
username = first_name[0].lower() + last_name.lower()

#Format full name
full_name = (first_name + " " + last_name).title()

#Clean up the bio
clean_bio = bio.strip()

#Count characters in the bio
bio_length = len(clean_bio)

#Replace "i am " with "i'm"
formatted_bio = clean_bio.replace("i am", "I'm")


#Display results 
print("_\n==== USER PROFILE ====")
print(F"fULL NAME: {full_name}")
print(f"Username: {username}")
print(f"Bio: {formatted_bio}")
print(f"Bio Length:  {bio_length} characters")