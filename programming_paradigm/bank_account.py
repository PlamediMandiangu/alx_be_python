# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes the bank account with a starting balance."""
        self._account_balance = initial_balance  # Use _ to denote private variable

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account if sufficient funds are available."""
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Displays the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")

