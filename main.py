from helpers import add, subtract, multiply, divide

def calculator():
    print("\n=== SIMPLE CALCULATOR ===")

    # Infinite loop so user can do multiple calculations
    while True:
        # Ask user for operation or exit option
        op = input("\nEnter operation (+, -, *, /) or 'b' to go back: ")

        if op.lower() == "b":
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

# Decide which math operation to perform
        if op == "+":
            print(f"{a} + {b} = {add(a, b)}")
        elif op == "-":
            print(f"{a} - {b} = {subtract(a, b)}")
        elif op == "*":
            print(f"{a} * {b} = {multiply(a, b)}")
        elif op == "/":
            print(f"{a} / {b} = {divide(a, b)}")
        else:
            # Handles invalid input like %, x, letters, etc.
            print("Invalid operation!")

# Convert numeric score into letter grade
def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

def grade_calculator():
    print("\n=== GRADE CALCULATOR ===")
    num_scores = int(input("How many test scores? "))

    total = 0 # store sum of all scores

    # Loop through each score input
    for i in range(num_scores):
        score = int(input(f"Enter score {i+1}: "))
        total += score

    average = total / num_scores
    grade = get_grade(average)

    print("\nResults:")
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Final Grade:", grade)

import random

def motivation():
    quotes = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "It always seems impossible until it’s done. - Nelson Mandela",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James"
]

    print("\nToday's Motivation:")
    print(random.choice(quotes))

def budget_tracker():
    budget = float(input("Enter your monthly budget: "))
    total_expenses = float(input("Enter your total expenses: "))

    balance = budget - total_expenses

    print("\n=== BUDGET SUMMARY ===")
    print("Budget:", budget)
    print("Total Expenses:", total_expenses)
    print("Balance:", balance)

    if balance > 0:
        print("You are UNDER budget by:", balance)
    elif balance < 0:
        print("You are OVER budget by:", abs(balance))
    else:
        print("You are exactly on budget.")

# ===== MAIN MENU =====
while True:
    print("\n====== MAIN MENU ======")
    print("1. Calculator")
    print("2. Grade Calculator")
    print("3. Motivation")
    print("4. Budget Tracker")
    print("5. Exit")


# Get user's choice as input
    choice = input("Choose an option: ")

# If user selects 1, run calculator function
    if choice == "1":
        calculator()

# If user selects 2, run grade calculator function
    elif choice == "2":
        grade_calculator()

# If user selects 3, show motivational quote
    elif choice == "3":
        motivation()

# If user selects 4, run budget tracker      
    elif choice == "4":
        budget_tracker()

# If user selects 5, exit the program
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Try again.")
