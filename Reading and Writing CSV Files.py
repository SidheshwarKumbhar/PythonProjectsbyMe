"""-----------------------------------------------------------------------------------------------------------------
* starting by writing a CSV file. Here we will first create a sample data using a Python dictionary about the name
and age of students, and then I will store that Python dictionary into a CSV file.

-------------------------------------------------------------------------------------------------------------------"""
# writing a csv file
import pandas as pd
import csv
import json

"""
data = {"Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data)
data.to_csv("age_list.csv")
tables = data

print((data["Name"]))


import csv
csv_filename = 'my_file.csv'
with open(csv_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# reading a csv file

#data = pd.read_csv("age_list.csv")
#print(data)


data = {"Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data)
data.to_csv("age_list.csv")
print(data)

csv_filename = 'age_list.csv'
with open('age_list.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

data = {"Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data, index=pd.RangeIndex(start=1, stop=6, name='sr_no'))
data.to_csv("age_list.csv")

data_dict = {}

# Step 2
# open a csv file handler
with open("age_list.csv", encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)

    # convert each row into a dictionary
    # and add the converted data to the data_variable

    for rows in csv_reader:
        # assuming a column named 'No'
        # to be the primary key
        key = rows["sr_no"]
        data_dict[key] = rows

print(data_dict)






#cute 1
"""
data = {"sr_no": [1, 2, 3, 4, 5],
        "Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data)
data.to_csv("age_list.csv", index=False)
rno = 5
rno -= 1
df = pd.read_csv("age_list.csv")
df.loc[rno, 'Name'] = 'SHIV CHANDRA'
df.to_csv("age_list.csv", index=False)

print(df)


"""

data = pd.read_csv("age_list.csv")
data = data.set_index("sr_no")
data = data.drop(4, axis=0)
data.to_csv("age_list.csv", index=False)

print(data)

def get_data():

    data_dict = {}
    with open("age_list.csv", encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        for rows in csv_reader:
            key = rows["sr_no"]
            data_dict[key] = rows

        json.dumps(data_dict, indent=4)
        return data_dict


col = get_data()
print(col)


a = "1234567"
print(type(a))

b = int(a)
print(type(b))
"""

#data = int(data)
#num = bin(num)[2:]