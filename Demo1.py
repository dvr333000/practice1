print("hello")

# Writing comment in python

# Variables
a = 3
print(a)

string = "Hello World"
string2 = 'Also works in single quote'
print(string)
print(string2)

a, b, c, d, e = 2, 2.5, 4, 'concat', "word"

print("Value of and c -", a+c)
# Above prints sum of a and c

print(d+' '+e)
# Above prints concat of d and e along with space in between d and e

print("Printing value a, b and d")
print(a, b, d)
# Above prints value of a, b and d

# Way of printing int and string using comma separated
print("{} {} {}".format("Value of a and b is ", a, b))

# print (a+"dfdfd"+c) integer/float string concatenation is not allowed using , operator
# but only way is to use format function as described above

print(type(a))
print(type(b))
print(type(c))
