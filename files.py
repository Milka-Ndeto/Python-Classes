import os

#open file 
file = open ("documentspython.txt", "r")
print(file.readlines())

# Open the file in append mode
with open("documentspython.txt", "a") as file:
    # Add new lines
    file.write("This is a new line.\n")
    file.write("Another line is added here.\n")
    file.write("Lets learn.\n")
    file.write("\nI cant wait to build  a python project")

# Example in Real life: Add an expense
def add_expense(item, amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{item},{amount}\n")

# Calculate total expenses
def total_expenses():
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
        total = sum(float(line.strip().split(",")[1]) for line in expenses)
        print(f"Total Expenses: ${total:.2f}")

# Example usage
add_expense("Lunch", 10.5)
add_expense("Transport", 4.2)
total_expenses()

# delete a file
# Specify the file path
file_path = "expenses.txt"

# Check if the file exists before attempting to delete it
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file {file_path} has been deleted.")
else:
    print(f"The file {file_path} does not exist.")





