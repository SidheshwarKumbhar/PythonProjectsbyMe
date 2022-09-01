"""-------------------------------------------------------------------------------------------------------------
* Age Calculator is an application where a user enters his date of birth as an input, and the application gives
 his age as an output.
---------------------------------------------------------------------------------------------------------------"""
import datetime

def ageCalculator(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365)
    print("Your age is ", age)


ageCalculator(1998, 10, 12)
