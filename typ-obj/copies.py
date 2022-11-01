a = [1 ,2, 3, [4,5] ]
b = list(a)
b is a

# False

b.append(100)
print(a)
print(b)

a.append(3)
print(a)

# a is unchanged


