a = 32
b = a
c = []
c.append(b)    # all this code creates value for a single object

# Reference - counting

# An object reference count is decreased with the del() built-in function

b = 31 
c[0] = 2.0

a = 37
import sys
print(sys.getrefcount(a))


# deleting the reference - count

a = {}
b = {}
a['b'] = b
b['a'] = a
del a

print(sys.getrefcount(b))








































