a = {'id': 89, 'name': "John", 'projects': [1, 2, 3, 4],
     'friends': [{'id': 82, 'name': "Bob"}, {'id': 83, 'name': "Amy"}]}
print(a.get('friends')[-1].get("name"))

for i in range(2, 10, 2):
    print(i, end="-")


a = [1, 2, 3, 4]
a[2] = 10
print(a)

a = 12
if a > 2:
    if a % 2 == 0:
        print("Tech")
    else:
        print("C is fun")
else:
    print("School")

print("{:d} Mission street, {}".format(972, "San Francisco"))

# 10. Which symbol should I use to redirect the error output to the standard output?
# Score: 0.0

# 2>&1
# 1>&2
# 2>
# I don't know
