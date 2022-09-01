"""-----------------------------------------------------------------------------------------------------------------
* starting by writing a CSV file. Here we will first create a sample data using a Python dictionary about the name
and age of students, and then I will store that Python dictionary into a CSV file.

-------------------------------------------------------------------------------------------------------------------"""
# writing a csv file
import pandas as pd

data = {"Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data)
data.to_csv("age_list.csv", index=False)
print(data.head())

# reading a csv file

data = pd.read_csv("age_list.csv")
print(data.head())

