items = {
'a' : 1,
'b' : 2,
'c': 3
    }

items["func"] = abs   # add a function
import math
items["mod"] = math   # Add a module
items["error"] = ValueError # Add an exception type
nums = [1,2,3,4]
items["append"] = nums.append  # Add a method of another object



# Now items dictionary contains: A function, a module, an exception and a method

print(items["func"](-45))
print(items["mod"].sqrt(4))

try: 
    x = int("Too much")
except items["error"] as e:
    print("Couldn't convert")

print(items["append"](100))
print(nums)
