import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# Ahmend's Financial Statement

budget = int(input("Enter your budget: "))
# budget = 50000
marketingCost = int(0.25 * budget)
operationalExpenses = int(0.5 * budget)
totalExpenses = int(operationalExpenses + marketingCost)
customerAqcuisition = int(0.25 * budget)

customers = int(customerAqcuisition / 5)
print(f"{Fore.YELLOW} The number of customers aqcuired were {customers}")
print(f"{Fore.YELLOW} Your total costs were {totalExpenses}")
print(f"{Fore.YELLOW} Marketing - {marketingCost}")
print(f"{Fore.YELLOW} Operations - {operationalExpenses}")
print ("---------------------------------- Done with Ahmed's Financial Statement ------------------------------------------------")


# For and while loop for printing even numbers from 1-30

# Starting with the for loop
for evenNumbers in range (31):
    if evenNumbers % 2 == 0:
        print(f"{Fore.GREEN} {evenNumbers} even numbers")
print ("---------------------------------- Done with even numbers using for loop ------------------------------------------------")

# the while loop is next
evenTwo = 0
while evenTwo <= 30:
    if evenTwo % 2 == 0:
        print(f"{Fore.GREEN} {evenTwo} Even Numbers")
    evenTwo += 1
print ("---------------------------------- Done with even numbers using while loop ------------------------------------------------")


# For and while loop for printing odd numbers from 1-30

# Starting with the for loop
for evenNumbers in range (31):
    if evenNumbers % 2 != 0:
        print(f"{Fore.CYAN} {evenNumbers} Odd numbers")
print ("---------------------------------- Done with odd numbers using for loop ------------------------------------------------")

# the while loop is next
evenTwo = 0
while evenTwo <= 30:
    if evenTwo % 2 != 0:
        print(f"{Fore.CYAN} {evenTwo} Odd Numbers")
    evenTwo += 1
print ("---------------------------------- Done with odd numbers using while loop ------------------------------------------------")