# Important modules
import os
import json
import sys
from math import sqrt, cos, sin, tan
# Unimportant module
from time import sleep
# Making a digit limit so the user can make huge calculations without the system crashing in a OverFlow Error
sys.set_int_max_str_digits(50000)
# Create the class that handles the calculations
class Calculator:
    # Initialize each variable thats gonna be used in this class
    def __init__(self, operation, previous_answer, history, x, y):
        self.operation = operation
        self.previous_answer = previous_answer
        self.history = history
        self.x = x
        self.y = y
    # Create a function that makes addition and adds it to the history
    def add(self):
        self.operation = f"{self.x} + {self.y}"
        self.previous_answer = self.x+self.y
        self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
        print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes subtraction and adds it to the history
    def subtract(self):
        self.operation = f"{self.x} - {self.y}"
        self.previous_answer = self.x-self.y
        self.history.append({"Operation": self.operation, "Answer": self.previous_answer})        
        print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes multiplication and adds it to the history
    def multiply(self):
        self.operation = f"{self.x} X {self.y}"
        self.previous_answer = self.x*self.y
        self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
        print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes division, handles zero division and adds it to the history
    def divide(self):
        try:
            self.operation = f"{self.x} / {self.y}"
            self.previous_answer = self.x/self.y
            self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
            print(f"\n{self.operation} = {self.previous_answer}")
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero")
    # Create a function that makes floor division, handles zero division and adds it to the history
    def floor_divide(self):
        try:
            self.operation = f"{self.x} // {self.y}"
            self.previous_answer = self.x//self.y
            self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
            print(f"\n{self.operation} = {self.previous_answer}")
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero")
    # Create a function that makes remainder division, handles zero division and adds it to the history
    def remainder(self):
        try:
            self.operation = f"{self.x} % {self.y}"
            self.previous_answer = self.x%self.y
            self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
            print(f"\n{self.operation} = {self.previous_answer}")
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero")
    # Create a function that makes exponents, handles zero getting raised to a negative number and adds it to the history
    def exponent(self):
        try:
            self.operation = f"{self.x} ^ {self.y}"
            self.previous_answer = self.x**self.y
            self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
            print(f"\n{self.operation} = {self.previous_answer}")
        except ZeroDivisionError:
            print("\nError: Zero cannot be raised to a negative number")
        except:
            if self.x == 0 and self.y == 0:
                pass
    # Create a function that makes square roots of the first number, handles negative number square rooting and adds it to the history
    def square_root_x(self):
        if self.x < 0:
            print("\nError: Negative number cannot have a square root")
        else:
            self.operation = f"√{self.x}"
            self.previous_answer = sqrt(self.x)
            self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
            print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes square roots of the second number, handles negative number square rooting and adds it to the history
    def square_root_y(self):
        if self.y < 0:
            print("\nError: Negative number cannot have a square root")
        else:
            self.operation = f"√{self.y}"
            self.previous_answer = sqrt(self.y)
            self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
            print(f"\n{self.operation} = {self.previous_answer}")  
    # Create a function that makes absolute values of the first number and adds it to the history
    def absolute_value_x(self):
       self.operation = f"|{self.x}|"
       self.previous_answer = abs(self.x)
       self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
       print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes absolute values of the second number and adds it to the history
    def absolute_value_y(self):
       self.operation = f"|{self.y}|"
       self.previous_answer = abs(self.y)
       self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
       print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes the sine value of the first number and adds it to the history
    def sin_x(self):
       self.operation = f"sin({self.x})"
       self.previous_answer = sin(self.x)
       self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
       print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes the sine value of the second number and adds it to the history
    def sin_y(self):
       self.operation = f"sin({self.y})"
       self.previous_answer = sin(self.y)
       self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
       print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes the cosine value of the first number and adds it to the history
    def cos_x(self):
       self.operation = f"cos({self.x})"
       self.previous_answer = cos(self.x)
       self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
       print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes the cosine value of the second number and adds it to the history
    def cos_y(self):
       self.operation = f"cos({self.y})"
       self.previous_answer = cos(self.y)
       self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
       print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes the tangent value of the first number and adds it to the history
    def tan_x(self):
       self.operation = f"tan({self.x})"
       self.previous_answer = tan(self.x)
       self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
       print(f"\n{self.operation} = {self.previous_answer}")
    # Create a function that makes the tangent value of the second number and adds it to the history
    def tan_y(self):
       self.operation = f"tan({self.y})"
       self.previous_answer = tan(self.y)
       self.history.append({"Operation": self.operation, "Answer": self.previous_answer})
       print(f"\n{self.operation} = {self.previous_answer}")
# Creating the class handles the history
class CalculatorHistory:
    # Initialize each variable thats gonna be used in this class
    def __init__(self, history, previous_answer):
        self.history = history
        self.previous_answer = previous_answer
    # Creating a function that reads data
    def read_data(self):
        # Checking if the file exists and assign the data to the variables
        if os.path.exists("Calculator2.json"):
            with open("Calculator2.json", "r") as f:
                self.history, self.previous_answer = json.load(f)
    # Creating a function that writes data and exits from the program
    def write_data_exit(self):
        print("Ok wait a moment...")
        sleep(1.5)
        print("Saving data...")
        sleep(2)
        with open("Calculator2.json", "w") as f:
            json.dump((self.history, self.previous_answer), f)
        print("Exiting...")
        sleep(1.5)
# Creating the class that is responsible for the user input and etc.
class CalculatorCLI:
    # Initializing each variable thats gonna be used in this class
    def __init__(self, option, history, previous_answer, x, y):
        self.option = option
        self.history = history
        self.previous_answer = previous_answer
        self.x = x
        self.y = y
    # Creating a function that asks for the numbers
    def ask_num(self):
        while True:
            try:
                self.x = float(input("Enter the first number ->: "))
                self.y = float(input("Enter the second number ->: "))
                break
            except ValueError:
                print("Invalid choice")
    # Creating a function that displays the menus and options
    def display_menu(self):
        CalculatorHistory.read_data(self)
        self.ask_num()
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
            print("10. Trigonometry operations(sin, cos, tan)")
            print("11. Enter new numbers")
            print("12. Use the previous answer with a new number")
            print("13. View history")
            print("14. Delete from history")
            print("15. Clear history")
            print("16. Exit")
            self.option = input("Enter your choice(1-16) ->: ")
            if self.option == '1':
                Calculator.add(self)
            elif self.option == '2':
                Calculator.subtract(self)
            elif self.option == '3':
                Calculator.multiply(self)
            elif self.option == '4':
                Calculator.divide(self)
            elif self.option == '5':
                Calculator.floor_divide(self)
            elif self.option == '6':
                Calculator.remainder(self)
            elif self.option == '7':
                Calculator.exponent(self)
            elif self.option == '8':
                sqrt_option = input(f"Would you like the square root of {self.x} or {self.y}?(Enter x for {self.x} y for {self.y}) ->: ").lower().strip()
                if sqrt_option == 'x':
                    Calculator.square_root_x(self)
                elif sqrt_option == 'y':
                    Calculator.square_root_y(self)
                else:
                    print("\nInvalid option")
            elif self.option == '9':
                abs_option = input(f"Would you like the absolute value of {self.x} or {self.y}?(Enter x for {self.x} y for {self.y}) ->: ").lower().strip()
                if abs_option == 'x':
                    Calculator.absolute_value_x(self)
                elif abs_option == 'y':
                    Calculator.absolute_value_y(self)
                else:
                    print("\nInvalid option")
            elif self.option == '10':
                trigonometry_option = input(f"Would you like a specific trigonometry value of {self.x} or {self.y}?(Enter x for {self.x} y for {self.y}) ->: ").lower().strip()
                if trigonometry_option == 'x':
                    trigonometry_operation = input(f'Would you like the sine, cosine or tangent of {self.x}?(sin for sine, cos for cosine, tan for tangent) ->: ').lower().strip()
                    if trigonometry_operation == 'sin':
                        Calculator.sin_x(self)
                    elif trigonometry_operation == 'cos':
                        Calculator.cos_x(self)
                    elif trigonometry_operation == 'tan':
                        Calculator.tan_x(self)
                    else:
                        print("\nInvalid option")
                elif trigonometry_option == 'y':
                    trigonometry_operation = input(f'Would you like the sine, cosine or tangent of {self.y}?(sin for sine, cos for cosine, tan for tangent) ->: ').lower().strip()
                    if trigonometry_operation == 'sin':
                        Calculator.sin_y(self)
                    elif trigonometry_operation == 'cos':
                        Calculator.cos_y(self)
                    elif trigonometry_operation == 'tan':
                        Calculator.tan_y(self)
                    else:
                        print("\nInvalid option")
                else:
                    print("\nInvalid option")
            elif self.option == '11':
                self.ask_num()
            elif self.option == '12':
                if self.previous_answer == None:
                    print("\nMake an operation to initialize the previous answer")
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
                    print("\nHistory: \n")
                    # Display
                    print("Position          Operation          Answer")
                    # Loop through each history information
                    position = 0
                    for history_data in self.history:
                        position += 1
                        print(f'{position}.                 {history_data["Operation"]}        {history_data["Answer"]}')
            elif self.option == '14':
                # Check if history data exists
                if not self.history:
                    print("\nNo data found to proceed")
                    print("Just a heads up if you don't remember what you want to delete remember to use choice 13")
                else:
                    # Storing positions in a list to handle unfound inputs
                    positions = [position+1 for position in range(len(self.history))]
                    while True:
                        try:
                            position = int(input("Enter the position that you would like to delete ->: "))
                            break
                        except ValueError:
                            print("Invalid choice")
                    # Check if the position exists
                    if position not in positions:
                        print("\nNo such position found")
                    else:
                        for history_data in self.history:
                            if (self.history.index(history_data))+1 == position:
                                self.history.remove(history_data)
                                print(f'\nThe operation {history_data["Operation"]} has been successfully deleted')
                                break
                            else:
                                continue
            elif self.option == '15':
                # Check if history data exists
                if not self.history:
                    print("\nNo data found to proceed")
                else:
                    self.history.clear()
                    print(f"\nThe history has been successfully cleared")
            elif self.option == '16':
                CalculatorHistory.write_data_exit(self)
                break
            else:
                print("\nInvalid choice")

calculator = CalculatorCLI(None, [], None, None, None)
calculator.display_menu()

                    

                            
