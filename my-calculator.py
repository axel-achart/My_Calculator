import csv

def number():
    while True:
        try:
            num1 = float(input("Enter the 1st  number : "))
            num2 = float(input("Enter the 2nd  number : "))
            return num1, num2
        except ValueError:
            print("enter a number")

def verif_Number(num_tuple):
    numb1= num_tuple[0]
    numb2 = num_tuple[1]

    if numb1 == int(numb1):
        numb1 = int(numb1)

        if numb2 == int(numb2):
            print("int")
            numb2 = int(numb2)
        elif numb2 == float(numb2):
            print("float")
            numb2 = float(numb2)

    elif numb1 == float(numb1):
        numb1 = float(numb1)

        if numb2 == float(numb2):
            numb2 = float(numb2)
        elif numb2 == int(numb2):
            numb2 = int(numb2)

    print(numb1, numb2)
    return numb1, numb2

def operation(format_tuple, signs):
    num_format1 = format_tuple[0]
    num_format2 = format_tuple[1]

    if signs == "+":
        return num_format1 + num_format2
    elif signs == "-":
        return num_format1 - num_format2
    elif signs == "/":
        return num_format1 / num_format2
    elif signs == "*":
        return num_format1 * num_format2

def display_result(result):
    print(f"here is your result : {result} ")

def add_hist(hist): 
    print(hist)
    with open('history.csv','w', newline='')as file:
        writter = csv.writer(file)
        writter.writerow(hist)

def show_hist():
    with open('history.csv', 'r') as file:
        read = csv.reader(file)
        for i in read:
            print(i)

def del_an_element(hist):
    while True:
        try:
            choice2 = int(input(f"enter a number between 0 and {len(hist)-1}"))
            del hist[choice2]
            with open('history.csv', 'w', newline='') as file:
                writter = csv.writer(file)
                writter.writerow(hist)
            break
        except ValueError:
            print("enter a number")
        except IndexError:
            print("enter the number between the interval")


def del_hist(hist):
    hist.clear()
    with open('history.csv', 'w',newline='') as file:
        writter = csv.writer(file)
        writter.writerow(hist)
    show_hist()
    

def main():
    history = []
    while True:
        print("""
            1 = use the calculator
            2 = show history
            3 = delete an element of your history
            4 = delete the entire history
            5 = exit your programmes
            """)
        try:
            choice = int(input("chose a number between 1 and 5 : "))
        ## choice_hist(choice)

            if choice == 1:
                number_tuple = number()
                format_number = verif_Number(number_tuple) #format verification int float

                sign = input("enter your sign : ")
                result = operation(format_number, sign)
                history.append(result)
                print(history)
                add_hist(history)
            
            if choice == 2:
                show_hist()
            
            if choice == 3:
                del_an_element(history)
            
            if choice == 4:
                del_hist(history)
            
            if choice == 5:
                break
            if choice > 5:
                print("enter a number < 5")
        except ValueError:
            print("please enter a number")

main()