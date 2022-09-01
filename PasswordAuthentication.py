"""---------------------------------------------------------------------------------------------------------
* A password authentication system is a system that is used for the identification of a user.
* this Password Authenticator asks for your email or a username, and then it asks for your password. If you
have entered the correct password then it verifies you as the real user.
* To create a password authentication system we have to follow the steps mentioned below:
    1. Create a dictionary of usernames with their passwords.
    2. Then you have to ask for user input as the username by using the input function in Python.
    3. Then you have to use the getpass module in Python to ask for user input as the password.
       Here we are using the getpass module instead of the input function to make sure that the user does not
       get to see what he/she write in the password field.
-------------------------------------------------------------------------------------------------------------"""
import getpass

database = {"aman.kharwal": "123456", "kharwal.aman": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password :")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")
