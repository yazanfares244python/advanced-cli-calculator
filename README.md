Advanced CLI Calculator

A feature-rich Command Line Interface (CLI) calculator built with Python. 
This project demonstrates clean input validation, robust error handling,
data serialization using JSON and memory management via operation tracking.

🚀 Features

Core Mathematics: Supports basic arithmetic (Addition, Subtraction, Multiplication, Division, Floor Division, Remainder, Exponents).
Advanced Logic: Includes Square Root calculations, Absolute Value tracking, and Trigonometric equations ($\sin$, $\cos$, $\tan$).
Data Persistence (JSON): Automatically saves and loads your calculation history and previous results across sessions using structural JSON serializatio.
Result Memory: Ability to pass the previous calculation's answer directly into a new operation.
Full History Management: View, clear, or target-delete individual lines of history securely.
Overflow Protection: Configured to handle ultra-high integer-to-string digit conversions (up to 50,000 digits) without crashing.
Error Prevention: Built-in safeguards against ZeroDivisionError, negative square roots, and invalid data inputs.🛠️ 
Tech Stack
Language: Python 3
Modules Used: math, json, os, sys, time
