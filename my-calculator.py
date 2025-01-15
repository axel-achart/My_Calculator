# BONUS : Fonctionnalité historique à votre calculatrice
# Possibilité d'effacer et réinitialiser l'historique
# (Pas de base de donnée)


# Function to Choose operation
def choose_operation():
    while True:
        try:
            print ("""Available operations :
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    5 - Exponentiation (Power of a number)
    6 - Quotient
    7 - Remainder
    8 - Exit""")

            operation = int(input("\nEnter your choice : "))

            if 1 <= operation <= 7:
                return operation        # Save type operation
            elif operation == 8:
                print("Leaving the calculator...")
                print()
                exit()      # To exit the program
            else:
                print("\nPlease enter a number between 1-7")

        except ValueError:
                print("\nPlease enter a number")


# Function to ask 2 numbers
def ask_numbers():
    while True:
        try:
            first_number = float(input("\nEnter the first number : "))
            second_number = float(input("Enter the second number : "))
            numbers = first_number, second_number
            return numbers

        except ValueError:
            print("Please enter a valid number")


# Calculation functions
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


# Menu 
def main(operation, numbers):
    while True:

        first_number, second_number  = numbers

        if first_number == int(first_number):       # verification if 1st numb is int
            first_number = int(first_number)

            if second_number == int(second_number):     # verification if 2nd numb is int
                second_number =  int(second_number)
            elif second_number == float(second_number):     # verification if 2nd numb is float
                second_number = float(second_number)

        elif first_number == float(first_number):       # verification if 1st numb is float
            first_number = float(first_number)

            if second_number == int(second_number):     # verification if 2nd numb is int
                second_number =  int(second_number)
            elif second_number == float(second_number):     # verification if 2nd numb is float
                second_number = float(second_number)
    

        operation = int(operation)      # operation --> int
        if operation == 1:
            print()
            print(first_number, '+', second_number, '=', addition(first_number, second_number))
            break

        elif operation == 2:
            print()
            print(first_number, '-', second_number, '=', subtraction(first_number, second_number))
            break
        
        elif operation == 3:
            print()
            print(first_number, '*', second_number, '=', multiplication(first_number, second_number))
            break
        
        elif operation == 4:
            print()
            print(first_number, '/', second_number, '=', division(first_number, second_number))
            break
        
        elif operation == 5:
            print()
            print(first_number, '**', second_number, '=', exponentiation(first_number, second_number))
            break
        
        elif operation == 6:
            print()
            print(first_number, '//', second_number, '=', quotient(first_number, second_number))
            break
        
        elif operation == 7:
            print()
            print(first_number, '%', second_number, '=', remainder(first_number, second_number))
            break


# Function to show the menu and execute the program
def menu():
    while True:
        print("\n--- MENU ---")
        main(choose_operation(), ask_numbers())


# Program execute only by myself
if __name__ == "__main__":
    print("\nLaunching the calculator...")
    menu()