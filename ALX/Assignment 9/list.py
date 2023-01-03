from unicodedata import lookup

suits = ['heart', 'diamond', 'spade', 'club']
nest = list(suits)
print(nest)
nest[0] = suits
print(nest)

suits.insert(2, 'Joker')
print(nest)
joke = nest[0].pop(2)
print(nest)
print(suits is nest[0])
print(suits is ['heart', 'diamond', 'spade', 'club'])
print(dict([(3, 9), (4, 16), (5, 25)]))

# [lookup('WHITE ' + s.upper() + ' SUIT') for s in suits]
# ['♡', '♢', '♤', '♧']
# print(lookup())