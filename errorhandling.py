# Corrected ZeroDivisionError handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.connection = None  # Simulating a database connection

    def connect_to_database(self):
        # Simulate opening a connection to a database
        self.connection = "Database connection established"
        print(self.connection)

    def close_connection(self):
        # Simulate closing a database connection
        if self.connection:
            print("Closing database connection.")
            self.connection = None

    def withdraw(self, amount):
        try:
            # Simulate connecting to the database
            self.connect_to_database()

            # Check if there are sufficient funds
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            
            # Perform the withdrawal
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        
        except ValueError as e:
            # Handle insufficient funds exception
            print(f"Error: {e}")
        
        except Exception as e:
            # Handle any other unexpected exceptions
            print(f"An unexpected error occurred: {e}")
        
        finally:
            # This block will always execute, even if an exception occurs
            self.close_connection()
            print("Thank you for banking with us.")

# Creating an account with an initial balance of 500
account = BankAccount(500)

# Trying to withdraw an amount
account.withdraw(200)  # Successful withdrawal
account.withdraw(1000)  # Insufficient funds
