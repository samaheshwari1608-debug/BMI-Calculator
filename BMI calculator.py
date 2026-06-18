# Creating a BMI calculator:
weight_gram= float(input("Enter Your Weight in gram:\n"))
height_cm= float(input("Enter Your Height in centimeter:\n"))
weight_kg= weight_gram/1000
height_m= height_cm/100
BMI= (weight_kg/(height_m*height_m))
print("Your BMI is", BMI)
if BMI < 18.5:
    print("You have falling in the underweight range")
elif 18.5 <= BMI <= 24.9:
    print("You have falling in the normal weight range")
elif 25 <= BMI <= 29.9:
    print("You have falling in the overweight range")
else:
    print("You have falling in the obesity range")