"""===================================================================================================================
* The Body Mass Index or BMI is calculated from weight and height of a Person.
* The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters,
then dividing the answer again by their height
===================================================================================================================="""
weight = float(input("Please enter your weight in KG :"))
height = float(input("Please enter your height in Feet:"))

height_in_meters = height * 0.3048
bmi = weight / (height_in_meters ** 2)
print("Your BMI is ", (round(bmi, 2)))

if bmi <= 18.4:
    print("Your BMI status is 'Underweight'.")
elif bmi <= 24.9:
    print("Your BMI status is 'Normal'.")
elif bmi <= 39.9:
    print("Your BMI status is 'Over Weight'.")
elif bmi > 40:
    print("Your BMI status is 'Obese'.")
