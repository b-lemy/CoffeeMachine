# The best package dealing with pandas

import pandas

data = pandas.read_csv('weather-data.csv')
# Get data in Columns
print(data['temp'])
# or
print(data.temp)

data_dict = data.to_dict()
print(data_dict)

data_list = data['temp'].to_list()
print(len(data_list))

avg = sum(data_list) / len(data_list)
print(avg)

# or
print(data['temp'].mean())
print(data['temp'].max())

# GET DATA IN ROWS
print(data[data.day == 'Monday'])