name = "Peru"
age = 26
stipend = 600.0
a = 4
b = "6"
c = str(a) + b
d = a + int(b)

print(f"Hello {name}! You are {age} years old. You earn {stipend} cedis every month.")

# Explicit casting, changing the ing age into a string before printing
print("Hello, my name is " + name + " and I am " + str(age)) 
print (c, d)

if age == a:
    print("these numbers are equal")
else:
    print("these numbers are not equal")

a = 46

# and logical operators
if age == a and age >= a:
    print("this is true")
else:
    print("This some bs")

# or logical operators
if age != a or age <= a:
    print ("This totally works")

num = 5
while num <= 5:
    print (num)
    num += 1