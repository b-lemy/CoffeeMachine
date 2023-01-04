from matrices import *
import string


def make_matrix(rows, columns):
    return [[0] * columns] * rows


m = make_matrix(4, 3)
print(m)

m[1][2] = 7
print(m)
# [[0, 0, 7], [0, 0, 7], [0, 0, 7], [0, 0, 7]]


# words = ['crunchy', 'raw', 'unboned', 'real', 'dead', 'frog']
# string.join(words, ' ')
# 'crunchy raw unboned real dead frog'
# string.join(words, '**')
# 'crunchy**raw**unboned**real**dead**frog'


for i in range(10, 0, -2):
    print(i)

this = ['I', 'am', 'not', 'a', 'crook']
that = ['I', 'am', 'not', 'a', 'crook']
print("Test 1: %s" % (this is that))
that = this
print("Test 2: %s" % (this is that))
