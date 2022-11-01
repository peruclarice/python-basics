# abc stands for abstract base class
# abstractmethod is a decorater, which is used as meta information

from abc import ABC, abstractmethod 

class User():
    userId = 0
    firstName = ""
    lastName = ""
    email = ""
    phone = ""
    password = ""

class UserAbstract(ABC):
    @abstractmethod
    def createUser(self, user : User):
        pass

    @abstractmethod
    def getAllUserInfo(self):
        pass

    @abstractmethod
    def getUserById(self, userId):
        pass

class UserManager(UserAbstract):
    def createUser(self, user : User):
        print("Creating Your User Information.... \n")
        print(f"First Name: {user.firstName}")
        print(f"Last Name: {user.lastName}")
        print(f"Email: {user.email}")
        print(f"Phone Number: {user.phone}")
        print(f"Password: {user.password}")

    def getAllUserInfo(self):
        print("Hello, this is where we get all user information")

    def getUserById(self, userId):
        print("Getting user by ID")

userManager = UserManager()
userManager.getAllUserInfo()
userManager.getUserById(900)

user = User()
user.firstName = "Clarice"
user.lastName = "Peru"
user.email = "peru@gmail.com"


userManager.createUser(user)

# Implement an abstract class called productAbstract
# Implement a class called productManager inheriting from the abstract class
# Create multiple sensible methods