# Geade Classifier

# Collect learner details
name = input("Enter learner name: ")

Subject1 = float(input("Enter the subject1 mark: "))
Subject2 = float(input("Enter the subject2 mark: "))
Subject3 = float(input("Enter the subject3 mark: "))

# Calculate average
average = (Subject1 + Subject2 + Subject3) / 3

# Assign avarage
if average >=80:
   grade = "A"
elif average >70:
   grade = "B"  
elif average >60:
   grade = "C"
elif average >50:
   grade = "D"     
else:
   grade = "F"  

   # Assign pass/fail status 
if average >=50:
      status = "Pass" 
else:
      status = "Fail"

 # Display report card
print("\n========== REPORT CARD ==========")    
print("Learner Name", name)
print("Subcject1:", Subject1)
print("Subcject2:", Subject2)
print("Subcject3:", Subject3)
print("Average:", round(average, 2))     
print("Grade:", grade)  
print("Status:", status)

# Intervation flags
if Subject1 < 40:
   print("Subject 1: Needs Intervertion")
if Subject2 < 40:
    print("Subject 2: Needs Intervation") 
if  Subject3 < 40:
    print("Subject 3: Needs Intervation") 

    print("===================================")