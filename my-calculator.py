# BONUS : Fonctionnalité historique à votre calculatrice
# Possibilité d'effacer et réinitialiser l'historique
# (Pas de base de donnée)



# Function to Choose operation
def choose_operation():
    while True:
        try:
            print ("""\nAvailable operations :
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
                print("Please enter a number between 1-7")

        except ValueError:
                print("Please enter a number")


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
        first_number = float(first_number)      # 1st number --> float
        second_number = float(second_number)        # 2nd number --> float
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
        print("\nLaunching the calculator...")
        print("\n--- MENU ---")
        main(choose_operation(), ask_numbers())


# Program execute only by myself
if __name__ == "__main__":
    menu()