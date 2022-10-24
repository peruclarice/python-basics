# users = {"Mandela","Siri","Chechi"}

# for user in users:
#     print(f"Hello {user}")

# Print even numbers
# Print with while loop from 1:30
allNumbers = int(input("Enter your number: "))

while allNumbers <= 30:
    if (allNumbers % 2 == 0):
        print (f"{allNumbers} is even")
    else:
        print(f"{allNumbers} is odd")
    allNumbers += 1
# print("This is beyond 30")

# Print with for loop from 1:30
newNumber = allNumbers
print(f"{newNumber} is the new number")
