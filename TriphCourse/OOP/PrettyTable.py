from prettytable import PrettyTable

# Tapping in methods
table = PrettyTable()
table.add_column('Pokemon_name', ['Results', 'pikachu'])
table.add_column('Type', ['Water', 'Air'])

# Tapping in attributes
table.align = 'l'
print(table)
