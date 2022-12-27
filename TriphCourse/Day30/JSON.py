import json

# Data to be written
dictionary = {
    "name": "Nisha",
    "rollno": 420,
    "cgpa": 10.10,
    "phonenumber": "1234567890"
}
#
# with open("sample.json", "w") as outfile:
#     # Write data to a json file
#     json.dump(dictionary, outfile, indent=4)
#
# To read the json data we use json.load
with open("sample.json", "r") as outfile:
    # Write data to a json file
    data = json.load(outfile)
    print(data)

# changes the data to a  dictionary

# to add to the json we use json.update
#     data.update(new_data)


