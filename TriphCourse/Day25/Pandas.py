# with open('weather-data.csv') as data_file:
#     data = data_file.readlines()
#
#     print(data)


# or

import csv

with open('weather-data.csv') as data_file:
    data = csv.reader(data_file)
    temperature = []
    # for temp in temperature:
    #    print(temp[1])
    # print(data)
    for row in data:

        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)
