# Lists of student

students = [
    {"name": "Ayanda", "maths": 85, "english": 78, "science": 90},
    {"name": "Akhona", "maths": 60, "english": 55, "science": 58},
    {"name": "Thando", "maths": 45, "english": 50, "science": 40},
    {"name": "Alondwe", "maths": 95, "english": 88, "science": 91},
    {"name": "Sbonelo", "maths": 72, "english": 68, "science": 75}
]

results = []
total_average = 0
highest_mark = 0
lowest_mark = 100

# Process each student 
for student in students: 
    average = (student["maths"] + student["english"] + student["science"]) / 3

    # Grade and Status
    if average >= 75:
       grade = "A"
       status = "Pass"
    elif average >= 60:
         grade = "B"
         status = "Pass"
    elif average >= 50:
         grade = "C"
         status = "Pass"
    else:
         grade = "F"
         status = "Fail"

    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

    total_average += average

    # Highest_mark
    if average > highest_mark:
       lowest_mark = average

# Class statistics
class_average = total_average / len(students)

# Display report
print("==== CLASS REPORT ====")

for result in results:
    print("----------------------------")
    print("Name:", result["name"])
    print("Average:", round(result["average"], 2))
    print("Grade:", result["grade"])
    print("Status:", result["status"])

print("----------------------------")
print("class Average:", round(class_average, 2))
print("highest_mark:", round(highest_mark, 2))
print("lowest Average:", round(lowest_mark, 2))


# Search by student name 
while True:
      search = input("Enter a student name to seach (or type 'xit'): ")

      if search.lower() == "exit":
        break 

        found = False

for result in results:
        if  result["name:"].lower() == search.lower():
           print("\nStudent Found")
           print("name:", result["name"])
           print("Average:", round(result["average"], 2))
           print("Grade:", result["grade"])
           print("Status:", result["status"])
           found = True 

           break

        if not found:
          print("Student not found.")


