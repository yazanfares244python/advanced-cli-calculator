# Important modules
import os
import json
from math import sqrt, sin, cos, tan
import sys
# Unimportant module
from time import sleep
# Calculator class
class Calculator:
    # Initialize each variable
    def __init__(self, x, y, option, history, previous_answer):
        self.x = x
        self.y = y
        self.option = option
        self.history = history
        self.previous_answer = previous_answer
        if os.path.exists("Calculator2.json"):
            with open("Calculator2.json", "r") as f:
                self.history, self.previous_answer = json.load(f)
    # Function that displays the options, asks for an input and gives operations
    def display_options(self):
        # Check if data exists
        if os.path.exists("Calculator2.json"):
            with open("Calculator2.json", "r") as f:
                self.history, self.previous_answer = json.load(f)
        while True:
            print("\n1. Addition(+)")
            print("2. Subtraction(-)")
            print("3. Multiplication(X)")
            print("4. Division(/)")
            print("5. Floor division(//)")
            print("6. Remainder(%)")
            print("7. Exponent(^)")
            print("8. Square root(√)")
            print("9. Absolute value(|x|)")
            print("10. Trigonometry values(sin, cos, tan)")
            print("11. Enter new numbers")
            print("12. Use the previous answer with a new number")
            print("13. View history")
            print("14. Delete from history")
            print("15. Clear history")
            print("16. Exit")
            self.option = input("Enter your option(1-16) ->: ")
            if self.option == '1':
                operation = f"{self.x} + {self.y}"
                self.previous_answer = self.x+self.y
                self.history.append({"Operation": operation, "Answer": self.previous_answer})
                print(f"\n{operation} = {self.previous_answer}")
            elif self.option == '2':
                operation = f"{self.x} - {self.y}"
                self.previous_answer = self.x-self.y
                self.history.append({"Operation": operation, "Answer": self.previous_answer})
                print(f"\n{operation} = {self.previous_answer}")
            elif self.option == '3':
                operation = f"{self.x} X {self.y}"
                self.previous_answer = self.x*self.y
                self.history.append({"Operation": operation, "Answer": self.previous_answer})
                print(f"\n{operation} = {self.previous_answer}")
            elif self.option == '4':
                # Handling ZeroDivision Errors
                try:
                    operation = f"{self.x} / {self.y}"
                    self.previous_answer = self.x/self.y
                    self.history.append({"Operation": operation, "Answer": self.previous_answer})
                    print(f"\n{operation} = {self.previous_answer}")
                except ZeroDivisionError:
                    print("\nError: Cannot divide by zero")
            elif self.option == '5':
                # Handling ZeroDivision Errors
                try:
                    operation = f"{self.x} // {self.y}"
                    self.previous_answer = self.x//self.y
                    self.history.append({"Operation": operation, "Answer": self.previous_answer})
                    print(f"\n{operation} = {self.previous_answer}")
                except ZeroDivisionError:
                    print("\nError: Cannot divide by zero")
            elif self.option == '6':
                # Handling ZeroDivision Errors
                try:
                    operation = f"{self.x} % {self.y}"
                    self.previous_answer = self.x%self.y
                    self.history.append({"Operation": operation, "Answer": self.previous_answer})
                    print(f"\n{operation} = {self.previous_answer}")
                except ZeroDivisionError:
                    print("\nError: Cannot divide by zero")
            elif self.option == '7':
                if self.x == 0 and self.y == 0:
                    print("\n0 to the power of 0 is undefined")
                elif self.x == 0 and self.y < 0:
                    print("\nError: Zero cannot be raised to a negative power")
                else:
                    operation = f"{self.x} ^ {self.y}"
                    self.previous_answer = self.x**self.y
                    self.history.append({"Operation": operation, "Answer": self.previous_answer})
                    print(f"\n{operation} = {self.previous_answer}")
            elif self.option == '8':
                sqrt_option = input(f"Do you want the square root of {self.x} or {self.y}?(Enter x for {self.x} y for {self.y}) ->: ").lower().strip()
                if sqrt_option == 'x':
                    # Handling square rooting negative numbers
                    if self.x < 0:
                        print("\nError: Negative numbers cannot have a square root")
                    else:
                        operation = f"√{self.x}"
                        self.previous_answer = sqrt(self.x)
                        self.history.append({"Operation": operation, "Answer": self.previous_answer})
                        print(f"\n{operation} = {self.previous_answer}")
                elif sqrt_option == 'y':
                    # Handling square rooting negative numbers
                    if self.y < 0:
                        print("\nError: Negative numbers cannot have a square root")
                    else:
                        operation = f"√{self.y}"
                        self.previous_answer = sqrt(self.y)
                        self.history.append({"Operation": operation, "Answer": self.previous_answer})
                        print(f"\n{operation} = {self.previous_answer}")
                else:
                    print("\nInvalid option")
            elif self.option == '9':
                abs_option = input(f"Do you want the absolute value of {self.x} or {self.y}?(Enter x for {self.x} y for {self.y}) ->: ").lower().strip()
                if abs_option == 'x':
                    operation = f"|{self.x}|"
                    self.previous_answer = abs(self.x)
                    self.history.append({"Operation": operation, "Answer": self.previous_answer})
                    print(f"\n{operation} = {self.previous_answer}")
                elif abs_option == 'y':
                    operation = f"|{self.y}|"
                    self.previous_answer = abs(self.y)
                    self.history.append({"Operation": operation, "Answer": self.previous_answer})
                    print(f"\n{operation} = {self.previous_answer}")
            elif self.option == '10':
                trigonometry_option = input(f"Do you want the specific trigonometry value of {self.x} or {self.y}?(Enter x for {self.x} y for {self.y}) ->: ").lower().strip()
                if trigonometry_option == 'x':
                    trigonometry_operation = input(f"Do you want the sine, cosine or tangent for {self.x}?('sin' for sine, 'cos' for cosine 'tan' for tangent) ->: ").lower().strip()
                    if trigonometry_operation == 'sin':
                        operation = f"sin({self.x})"
                        self.previous_answer = sin(self.x)
                        self.history.append({"Operation": operation, "Answer": self.previous_answer})
                        print(f"\n{operation} = {self.previous_answer}")
                    elif trigonometry_operation == 'cos':
                        operation = f"cos({self.x})"
                        self.previous_answer = cos(self.x)
                        self.history.append({"Operation": operation, "Answer": self.previous_answer})
                        print(f"\n{operation} = {self.previous_answer}")
                    elif trigonometry_operation == 'tan':
                        operation = f"tan({self.x})"
                        self.previous_answer = tan(self.x)
                        self.history.append({"Operation": operation, "Answer": self.previous_answer})
                        print(f"\n{operation} = {self.previous_answer}")
                    else:
                        print("\nInvalid operation")
                elif trigonometry_option == 'y':
                    trigonometry_operation = input(f"Do you want the sine, cosine or tangent for {self.y}?('sin' for sine, 'cos' for cosine 'tan' for tangent) ->: ").lower().strip()
                    if trigonometry_operation == 'sin':
                        operation = f"sin({self.y})"
                        self.previous_answer = sin(self.y)
                        self.history.append({"Operation": operation, "Answer": self.previous_answer})
                        print(f"\n{operation} = {self.previous_answer}")
                    elif trigonometry_operation == 'cos':
                        operation = f"cos({self.y})"
                        self.previous_answer = cos(self.y)
                        self.history.append({"Operation": operation, "Answer": self.previous_answer})
                        print(f"\n{operation} = {self.previous_answer}")
                    elif trigonometry_operation == 'tan':
                        operation = f"tan({self.y})"
                        self.previous_answer = tan(self.y)
                        self.history.append({"Operation": operation, "Answer": self.previous_answer})
                        print(f"\n{operation} = {self.previous_answer}")
                    else:
                        print("\nInvalid operation")
                else:
                    print("\nInvalid choice")
            elif self.option == '11':
                while True:
                    try:
                        self.x = float(input("Enter the new first number ->: "))
                        self.y = float(input("Enter the new second number ->: "))
                        break
                    except ValueError:
                        print("Invalid choice")
            elif self.option == '12':
                if self.previous_answer == None:
                    print("\nMake at least one calculation to initialize the previous answer")
                else:
                    self.x = self.previous_answer
                    while True:
                        try:
                            self.y = float(input("Enter another number to use alongside the previous answer ->: "))
                            break
                        except ValueError:
                            print("Invalid choice")
            elif self.option == '13':
                # Check if history data exists
                if not self.history:
                    print("\nNo data found to proceed")
                else:
                    print("Position:         Operation:         Answer:")
                    for position in range(len(self.history)):
                            # The huge gaps are for better structure and orientation
                            print(f"{position+1}               {self.history[position]['Operation']}              {self.history[position]['Answer']}")
            elif self.option == '14':
                # Check if history data exists
                if not self.history:
                    print("\nNo data found to proceed")
                else:
                    # Storing taken ids to handle unfound ids
                    found_ids = [history_id+1 for history_id in range(len(self.history))]
                    # Making an input to validate if the user wants to continue
                    validate_input = input("Are you sure that you remember what you wanted to delete?(y/n) ->: ").lower().strip()
                    if validate_input == 'y':
                        print("Ok we will proceed")
                    elif validate_input == 'n':
                        print("\nOk we will not proceed")
                        continue
                    else:
                        print("\nInvalid choice")
                        continue
                    # Delete id input
                    while True:
                        try:
                            delete_id = int(input("Enter the id of the operation that you would like to delete from the history ->: "))
                            break
                        except ValueError:
                            print("\nInvalid choice")
                    # Check if the id exists
                    if delete_id not in found_ids:
                        print("\nNo such ID found")
                    else:
                        self.history.remove(self.history[delete_id-1])
                        print(f"\nThe operation with the id {delete_id} has been successfully deleted")
            elif self.option == '15':
                # Check if history data exists
                if not self.history:
                    print("\nNo data found to proceed")
                else:
                    # Making an input to validate if the user wants to continue
                    validate_input = input("Are you sure that you remember what you wanted to delete?(y/n) ->: ").lower().strip()
                    if validate_input == 'y':
                        print("Ok we will proceed")
                    elif validate_input == 'n':
                        print("\nOk we will not proceed")
                        continue
                    else:
                        print("\nInvalid choice")
                        continue
                    self.history.clear()
                    print(f"\nThe history has been successfully cleared")
            elif self.option == '16':
                print("Ok wait a moment...")
                sleep(1.5)
                print("Saving data...")
                with open("Calculator2.json", "w") as f:
                    json.dump((self.history, self.previous_answer), f)
                sleep(2)
                print("Exiting...")
                sleep(1.5)
                break
            else:
                print("\nInvalid choice")
# Ask for the numbers
while True:
    try:
        x = float(input("Enter the first number ->: "))
        y = float(input("Enter the second number ->: "))
        break
    except ValueError:
        print("Invalid choice")
calculator = Calculator(x, y, None, [], None)
calculator.display_options()

    
    