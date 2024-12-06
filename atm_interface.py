import random

class ATMInterface:
    def __init__(self):
        self.balance = round(random.uniform(0, 10000000.0), 2)  # Random balance between 0 and 10,000,000
        self.pin = 1234  # Default PIN
    
    def menu(self):
        print("WELCOME TO THE ATM")
        print("ATM MENU")
        print("PLEASE SELECT ONE OF THE FOLLOWING")
        print("1. CHECK BALANCE")
        print("2. DEPOSIT MONEY")
        print("3. WITHDRAW MONEY")
        print("4. CHANGE PIN")
        print("5. CANCEL TRANSACTION")
    
    def start_operation(self):
        self.menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.check_balance()
        elif choice == 2:
            self.deposit_money()
        elif choice == 3:
            self.withdraw_money()
        elif choice == 4:
            self.change_pin()
        elif choice == 5:
            print("Transaction Cancelled")
        else:
            print("Invalid Input")
    
    def check_balance(self):
        if self.check_pin():
            print(f"Your current balance is: Rs. {self.balance:.2f}")
            print("Transaction Completed")
        else:
            print("Wrong PIN Entered\nTransaction Cancelled")
    
    def deposit_money(self):
        deposit = float(input("Enter the deposit amount: "))
        if self.check_pin():
            self.balance += deposit
            print("Amount deposited successfully in your account.")
            print("Transaction Completed")
        else:
            print("Wrong PIN Entered\nTransaction Cancelled")
    
    def withdraw_money(self):
        if self.check_pin():
            withdraw = int(input("Enter the withdrawal amount: \nPlease enter in multiples of 500: "))
            if withdraw % 500 != 0:
                print("Please enter an amount in multiples of 500.")
                return
            if withdraw > self.balance:
                print("Insufficient Balance in your Account.")
            else:
                self.balance -= withdraw
                print("Amount withdrawal successful")
            show_balance = input("Would you like to display the Balance? (y/n): ").lower()
            if show_balance == 'y':
                self.check_balance()
            else:
                print("Transaction Completed")
        else:
            print("Wrong PIN Entered\nTransaction Cancelled")
    
    def change_pin(self):
        if self.check_pin():
            new_pin = int(input("ENTER YOUR NEW PIN: "))
            confirm_pin = int(input("CONFIRM YOUR PIN: "))
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully.")
                print("Transaction Completed")
            else:
                print("PIN mismatch! Transaction Cancelled")
        else:
            print("Wrong PIN Entered\nTransaction Cancelled")
    
    def check_pin(self):
        entered_pin = int(input("Enter your PIN: "))
        return entered_pin == self.pin

if __name__ == "__main__":
    atm = ATMInterface()
    atm.start_operation()