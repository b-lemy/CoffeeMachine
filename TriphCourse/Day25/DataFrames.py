import pandas

data = pandas.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

print(data[data["Primary Fur Color"] == 'Black'])
print(len(data[data["Primary Fur Color"] == 'Gray']))

data_dict = {
    'Fur_Color': ['1', '2', '3'],
    'Count': ['Red', 'Orange', 'Black']
}
df = pandas.DataFrame(data_dict)
df.to_csv('Trial.csv')


print(list(range(10, 0, -2)))

a = "Python is cool"
print(a[7:-5])
