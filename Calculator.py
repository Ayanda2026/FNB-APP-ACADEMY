# Multi-Function Calculator

# Get two numbers from the user
num1 = float(input("Enter the first numbber: "))
num2 = float(input("Enter the second numbber: "))

# Basic Oparations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Check if the second number is zero
if num2 != 0:
     division = round(num1 / num2, 2)
     floor_division = round(num1 // num2, 2)
     modulus = round(num1 % num2, 2)
else: 
     division = "Cannot be divided by zero"
     floor_division = "Cannot be divided by zero" 
     modulus = "Cannot be divided by zero"


# Display result using f-strings
print("\n========== CALCULATE RESULT ==========")
print(f"{'Oparation':<20}{'Result'}")
print("-" * 35)
print(f"{'Addition':<20}{addition}")
print(f"{'Subtraction':<20}{subtraction}")
print(f"{'Multiplication':<20}{multiplication}")
print(f"{'Division':<20}{division}")
print(f"{'Floor_division':<20}{floor_division}")
print(f"{'Modulus':<20}{modulus}")
print("=" * 35)


             