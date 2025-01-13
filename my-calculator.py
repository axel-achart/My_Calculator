# Demande à l'utilisateur : le type d'opération, deux nombres entiers/décimaux
# Gérer les éventuelles erreurs d'input
# math et eval() --> INTERDIT
#
# BONUS : Fonctionnalité historique à votre calculatrice
# Possibilité d'effacer et réinitialiser l'historique
# (Pas de base de donnée)
#
# +, -, *, /, %, //, **


def ask_numbers(first_number, second_number):
    while True:
        try:
            first_number = float(input("\nEnter the first number : "))
            second_number = float(input("Enter the second number : "))
            return first_number, second_number
        except ValueError:
            print("Please enter a valid number")


def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

def exponentiation(first_number, second_number):
    return first_number ** second_number

def quotient(first_number, second_number):
    return first_number // second_number

def remainder(first_number, second_number):
    return first_number % second_number


# Menu to choose operation
def menu(first_number, second_number):
    while True:
        try:
            print ("""\nAvailable operations :
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    5 - Exponentiation (Power of a number)
    6 - Quotient
    7 - Remainder""")

            operation = int(input("\nEnter your choice : "))

            if operation in (1, 2, 3, 4, 5, 7):
                if operation == 1:
                    ask_numbers(first_number, second_number)
                    print(first_number, '+', second_number, '=', addition(first_number, second_number))
                
                if operation == 2:
                    ask_numbers()
                    subtraction(first_number, second_number)
                
                if operation == 3:
                    ask_numbers()
                    multiplication(first_number, second_number)
                
                if operation == 4:
                    ask_numbers()
                    division(first_number, second_number)
                
                if operation == 5:
                    ask_numbers()
                    exponentiation(first_number, second_number)
                
                if operation == 6:
                    ask_numbers()
                    quotient(first_number, second_number)
                
                if operation == 7:
                    ask_numbers()
                    remainder(first_number, second_number)
            
            else:
                print("Please enter a number between 1-7")

        except ValueError:
            print("Please enter a valid value")



menu(first_number, second_number)