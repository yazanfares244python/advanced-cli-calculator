# Important modules
from math import sqrt, sin, cos, tan
import os
import json
import sys
# Unimportant module
from time import sleep
# To avoid OverFlow Error with big digits
sys.set_int_max_str_digits(50000)
# Main calculator function
def calculator():
    # Storing history in a list and the previous answer
    history = []
    previous_answer = None
    # Checking if data exists to save the old data
    if os.path.exists('Calculator.json'):
        with open('Calculator.json', 'r') as f:
            history, previous_answer = json.load(f)
    # Ask for the numbers and handling invalid inputs
    while True:
        try:
            x = float(input('Enter the first number ->: '))
            y = float(input('Enter the second number ->: '))
            break
        except ValueError:
            print('Invalid choice therefore we will restart')
    # Menu options
    while True:
        print('\nOptions: \n')
        print('1. Addition(+)')
        print('2. Subtraction(-)')
        print('3. Multiplication(X)')
        print('4. Division(/)')
        print('5. Floor division(//)')
        print('6. Remainder(%)')
        print('7. Exponent(^)')
        print('8. Square root(√)')
        print('9. Absolute value(|x|)')
        print('10. Trigonometry equations(sin, cos, tan)')
        print('11. Use the previous result with a new number')
        print('12. Enter new numbers')
        print('13. View history')
        print('14. Delete from history')
        print('15. Clear history')
        print('16. Exit')
        option = input("Enter your choice(1-16) ->: ")
        if option == '1':
            operation = f"{x} + {y}"
            previous_answer = x+y
            history.append({'Operation': operation, "Answer": previous_answer})
            print(f"\n{operation} = {previous_answer}")
        elif option == '2':
            operation = f"{x} - {y}"
            previous_answer = x-y
            history.append({'Operation': operation, "Answer": previous_answer})
            print(f"\n{operation} = {previous_answer}")
        elif option == '3':
            operation = f"{x} X {y}"
            previous_answer = x*y
            history.append({'Operation': operation, "Answer": previous_answer})
            print(f"\n{operation} = {previous_answer}")
        # Handling ZeroDivision Errors in choice 4, 5, 6
        elif option == '4':
            if y == 0:
                print("\nError: Cannot divide by zero")
            else:
                operation = f"{x} / {y}"
                previous_answer = x/y
                history.append({'Operation': operation, "Answer": previous_answer})
                print(f"\n{operation} = {previous_answer}")
        elif option == '5':
            if y == 0:
                print("\nError: Cannot divide by zero")
            else:
                operation = f"{x} // {y}"
                previous_answer = x//y
                history.append({'Operation': operation, "Answer": previous_answer})
                print(f"\n{operation} = {previous_answer}")
        elif option == '6':
            if y == 0:
                print("\nError: Cannot divide by zero")
            else:
                operation = f"{x} % {y}"
                previous_answer = x%y
                history.append({'Operation': operation, "Answer": previous_answer})
                print(f"\n{operation} = {previous_answer}")
        elif option == '7':
            if x == 0 and y == 0:
                print("\n0 to the power of 0 is undefined")
            else:
                operation = f"{x} ^ {y}"
                previous_answer = x**y
                history.append({'Operation': operation, "Answer": previous_answer})
                print(f"\n{operation} = {previous_answer}")
        elif option == '8':
            sqrt_option = input(f"Would you like the square root of {x} or {y}?(Enter x for {x} y for {y}) ->: ").lower().strip()
            if sqrt_option == 'x':
                if x < 0:
                    print("\nError: Negative numbers cannot have a square root") 
                else:
                    operation = f"√{x}"
                    previous_answer = sqrt(x)
                    history.append({'Operation': operation, "Answer": previous_answer})
                    print(f"\n{operation} = {previous_answer}")
            elif sqrt_option == 'y':
                if y < 0:
                    print("\nError: Negative numbers cannot have a square root") 
                else:
                    operation = f"√{y}"
                    previous_answer = sqrt(y)
                    history.append({'Operation': operation, "Answer": previous_answer})
                    print(f"\n{operation} = {previous_answer}")
            else:
                print("\nInvalid choice")
        elif option == '9':
            abs_option = input(f"Would you like the absolute value of {x} or {y}?(Enter x for {x} y for {y}) ->: ").lower().strip()
            if abs_option == 'x':
                operation = f"|{x}|"
                previous_answer = abs(x)
                history.append({'Operation': operation, "Answer": previous_answer})
                print(f"\n{operation} = {previous_answer}")
            elif abs_option == 'y':
                operation = f"|{y}|"
                previous_answer = abs(y)
                history.append({'Operation': operation, "Answer": previous_answer})
                print(f"\n{operation} = {previous_answer}")
            else:
                print("\nInvalid choice")
        elif option == '10':
            trigonometry_option = input(f"Would you like a specific trigonometry value of {x} or {y}?(Enter x for {x} y for {y}) ->: ").lower().strip()
            if trigonometry_option == 'x':
                trigonometry_operation = input(f"Would you like the sine, cosine, tangent of {x}? ->: ").lower().strip()
                if trigonometry_operation == 'sine':
                    operation = f"sin({x})"
                    previous_answer = sin(x)
                    history.append({'Operation': operation, "Answer": previous_answer})
                    print(f"\n{operation} = {previous_answer}")
                elif trigonometry_operation == 'cosine':
                    operation = f"cos({x})"
                    previous_answer = cos(x)
                    history.append({'Operation': operation, "Answer": previous_answer})
                    print(f"\n{operation} = {previous_answer}")
                elif trigonometry_operation == 'tangent':
                    operation = f"tan({x})"
                    previous_answer = tan(x)
                    history.append({'Operation': operation, "Answer": previous_answer})
                    print(f"\n{operation} = {previous_answer}")
                else:
                    print("\nInvalid choice")
            elif trigonometry_option == 'y':
                trigonometry_operation = input(f"Would you like the sine, cosine, tangent of {x}? ->: ").lower().strip()
                if trigonometry_operation == 'sine':
                    operation = f"sin({y})"
                    previous_answer = sin(y)
                    history.append({'Operation': operation, "Answer": previous_answer})
                    print(f"\n{operation} = {previous_answer}")
                elif trigonometry_operation == 'cosine':
                    operation = f"cos({y})"
                    previous_answer = cos(y)
                    history.append({'Operation': operation, "Answer": previous_answer})
                    print(f"\n{operation} = {previous_answer}")
                elif trigonometry_operation == 'tangent':
                    operation = f"tan({y})"
                    previous_answer = tan(y)
                    history.append({'Operation': operation, "Answer": previous_answer})
                    print(f"\n{operation} = {previous_answer}")
                else:
                    print("\nInvalid choice")
            else:
                print("\nInvalid choice")
        elif option == '11':
            # Check if there is a previous answer
            if previous_answer == None:
                print("\nMake at least one operation to initialize the previous answer")
            else:
                x = previous_answer
                while True:
                    try:
                        y = float(input("Enter another number to use alongside the prevous answers ->: "))
                        break
                    except ValueError:
                        print("Invalid choice")
        elif option == '12':
            # Ask for the numbers and handling invalid inputs AGAIN
            while True:
                try:
                    x = float(input('Enter the first number ->: '))
                    y = float(input('Enter the second number ->: '))
                    break
                except ValueError:
                    print('Invalid choice therefore we will restart')
        elif option == '13':
            # Check if data exists
            if not history:
                print('\nNo data found to proceed')
            else:
                print("\nHistory: \n")
                print("Position:   Operation:      Answer:    ")
                # Loop through each history info
                for history_info in history:
                    #                             This blank is for clearer structure 
                    print(f"{history.index(history_info)+1}.          {history_info['Operation']}    {history_info['Answer']}")
        elif option == '14':
            # Check if data exists
            if not history:
                print("\nNo data found to proceed")
                print("Just a heads up if you don't remember what you want to delete remember to use choice 13")
            else:
                # Found position in a list
                found_positions = [position+1 for position in range(len(history))]
                # Delete position input
                while True:
                    try:
                        delete_position = int(input("Enter the position that you would like to delete ->: "))
                        break
                    except ValueError:
                        print("Invalid choice")
                # Check if the operation exists
                if delete_position not in found_positions:
                    print("\nNo such position found")
                else:
                    # Loop through each history information
                    for history_info in history:
                        if history.index(history_info)+1 == delete_position:
                            history.remove(history_info)
                            print(f"\nThe position {delete_position} has been successfully deleted")
                            break
                        else:
                            continue
        elif option == '15':
            # Check if data exists
            if not history:
                print("\nNo data found to proceed")
            else:
                history.clear()
                print(f"\nThe history has been successfully cleared")
        elif option == '16':
            print("Ok wait a moment...")
            sleep(1.5)
            print("Saving data...")
            with open("Calculator.json", "w") as f:
                json.dump((history, previous_answer), f)
            sleep(2)
            print('Exiting...')
            sleep(1.5)
            break
        else:
            print("\nInvalid option")
if __name__ == '__main__':
    calculator()

                    

        
