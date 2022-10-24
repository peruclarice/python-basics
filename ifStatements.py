# firstName = input("What is your first name? ")
# secondName = input("What is your second name? ")

# first_char = firstName[0]
# if first_char == "P" or first_char == "p":
#     print("Welcome " + firstName + " " + secondName + " to the party")
# else:
#     print("You're name is not on the list " + firstName + " " + secondName + ", Sorry!")


# Accept two inputs, userName and password. Condition, userName is admin and password is 1234@admin
# Print a message that says "Hello, your are logged in as admin"
# Else say "Invalid username/password"

userName = input("Enter your username: ")
password = input("Enter your password: ")

if (userName == "Admin" and password == "1234@admin"):
    print("Hello, you are logged in as " + userName)
else:
    print("Invalid username/password")