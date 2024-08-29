#simple atm system
import sys

class Card:
    def __init__(self):
        self.pin = "8848"
        self.balance = 1000

    def withdraw(self, amount):
        self.balance -= amount

    def reset_pin(self, new_pin):
        self.pin = new_pin


def main():
    atm = Card()
    print("Enter 1 to Balance Inquiry \nEnter 2 to Withdraw Amount \nEnter 3 to Reset Pin \nEnter 4 to Cancel")
    option = input("Enter your Transaction: ")
    if option == "4":
        sys.exit("Transaction Cancelled.")
    else:
        get_pin = input("Enter your pin: ")
        try:
            validate_pin(atm.pin, get_pin)
            if option == "1":
                print(f"Your current balance is ${atm.balance}")
                sys.exit("Thank you have a good day. Please Collect your card")

            if option == "2":
                amount = float(input("Enter the amount to withdraw: "))
                try:
                    check_balance(atm.balance, amount)
                    atm.withdraw(amount)
                    print(f"${amount} withdrawn successfully. Please collect your cash")
                    print(f"Your remaining balance is ${atm.balance}")
                    sys.exit("Thank you have a good day. Please collect your card")
                except Exception:
                    sys.exit("You dont have sufficient balance")

            if option == "3":
                try:
                    new_pin = input("Enter your new pin: ")
                    confirm_pin = input("Confirm Your new pin: ")
                    check_pin(new_pin, confirm_pin)
                    atm.reset_pin(new_pin)
                    print("Your pin has been reset")
                    sys.exit("Thank you have a good day. Please collect your card")
                except Exception:
                    sys.exit("Couldn't confirm new pin!")
        except Exception:
            sys.exit("Entered wrong pin!")


def validate_pin(mypin, pin):
    if pin != mypin:
        raise ValueError

def check_balance(balance, amount):
    if amount > balance:
        raise ValueError

def check_pin(new_pin, confirm_pin):
    if new_pin != confirm_pin:
        raise ValueError

if __name__ == "__main__":
    main()
