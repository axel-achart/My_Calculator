# Function to Choose operation (1st launch)
def choose_operation():
    while True:
        try:
            print ("""Available operations :
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    5 - Power of a number
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
                print("\nPlease enter a number between 1-8")

        except ValueError:
                print("\nPlease enter a number")


# Function to ask 2 numbers (2nd launch)
def ask_numbers():
    while True:
        try:
            first_number = float(input("\nEnter the first number : "))
            second_number = float(input("Enter the second number : "))
            numbers = first_number, second_number
            return numbers

        except ValueError:
            print("Please enter a valid number")


# Calculation functions (use to calculate results)
def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

def power(first_number, second_number):
    return first_number ** second_number

def quotient(first_number, second_number):
    return first_number // second_number

def remainder(first_number, second_number):
    return first_number % second_number






# Function Show History
def display_hist(hist, result):
    hist.append(result)
    while True:
        try:
            show_hist = str(input("\nDo you want to show history ? (y/n) : "))
            if show_hist == 'y' or show_hist == 'yes':
                print("\nHistory :", hist)
                break
            elif show_hist == 'n' or show_hist == 'no':
                print("\nHistory not show")
                break
        except ValueError:
            print("\nPlease enter a valid value (y/n)")

# Function Delete an element
def delete_hist(hist):
    while True:
        try:
            remove = str(input("\nDo you want to remove an element from history ? (y/n) : "))
            if remove == 'y' or remove == 'yes':
                while True:
                    try:
                        delete = int(input(f"History contain {len(hist)} element(s), Enter the index of your choice (between 0 - {len(hist)-1}) : "))
                        del hist[delete]
                        print("\nHistory update : ", hist)
                        break
                    except ValueError:
                        print("\nPlease enter a valid number")
                    except IndexError:
                        print("\nPlease enter a valid index")
            elif remove == 'n' or remove == 'no':
                print("\nNo items deleted")
                break
        except ValueError:
            print("\nPlease enter a valid value (y/n)")

# Function to reset history
def reset_hist(hist):
    while True:
        try:
            ask_reset = str(input("\nDo you want to clear history ? (y/n) : "))
            if ask_reset == 'y' or ask_reset == 'yes':
                hist.clear()
                print()
                print(f"History update : {hist}")
                break
            elif ask_reset == 'n' or ask_reset == 'no':
                print("\nHistory not clear")
                break
        except ValueError:
            print("\nPlease enter a valid value (y/n)")




# Menu (3rd launch)
def main(operation, numbers, hist):

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
            result = addition(first_number, second_number)
            print(first_number, '+', second_number, '=', result)
            display_hist(hist, result)
            delete_hist(hist)
            reset_hist(hist)
            break

        elif operation == 2:
            print()
            result = subtraction(first_number, second_number)
            print(first_number, '-', second_number, '=', result)
            display_hist(hist, result)
            delete_hist(hist)
            reset_hist(hist)
            break
        
        elif operation == 3:
            print()
            result = multiplication(first_number, second_number)
            print(first_number, '*', second_number, '=', result)
            display_hist(hist, result)
            delete_hist(hist)
            reset_hist(hist)
            break
        
        elif operation == 4:
            print()
            while second_number != 0:
                result = division(first_number, second_number)
                print(first_number, '/', second_number, '=', result)
                display_hist(hist, result)
                delete_hist(hist)
                reset_hist(hist)
                break
            if second_number == 0:
                print("Impossible division with divider = 0, retry")
                break
        
        elif operation == 5:
            print()
            result = power(first_number, second_number)
            print(first_number, '**', second_number, '=', result)
            display_hist(hist, result)
            delete_hist(hist)
            reset_hist(hist)
            break
        
        elif operation == 6:
            print()
            while second_number != 0:
                result = quotient(first_number, second_number)
                print(first_number, '//', second_number, '=', result)
                display_hist(hist, result)
                delete_hist(hist)
                reset_hist(hist)
                break
            if second_number == 0:
                    print("Impossible division with divider = 0, retry")
                    break
        
        elif operation == 7:
            print()
            while second_number != 0:
                result = remainder(first_number, second_number)
                print(first_number, '%', second_number, '=', result)
                display_hist(hist, result)
                delete_hist(hist)
                reset_hist(hist)
                break
            if second_number == 0:
                    print("Impossible division with divider = 0, retry")
                    break


# Function to show the menu and execute the program
def menu():
    hist = []
    while True:
        print("\n--- MENU ---")
        main(choose_operation(), ask_numbers(), hist)


# Program execute only by myself
if __name__ == "__main__":
    print("\nLaunching the calculator...")
    menu()