# Simple Atm System
#### video url: https://youtu.be/SpgqSi7kkyk?si=8CaBecSEg3Lsswdj
#### Description:
This is a basic ATM system implemented in Python. It provides functionality for users to perform the following operations:

1.Check their account balance.
2.Withdraw money.
3.Reset their PIN.
4.Cancel the transaction.


Features
1.Balance Inquiry: Users can check their current account balance.
2.Withdraw Amount: Users can withdraw a specified amount from their account.
3.Reset PIN: Users can reset their PIN, provided they confirm the new PIN correctly.
4.Cancel: Users can cancel the transaction at any time.

## Code Explanation
Card Class:

__init__(): Initializes a card with a default PIN ("8848") and balance (1000).
withdraw(amount): Deducts the specified amount from the balance.
reset_pin(new_pin): Updates the card's PIN to the new PIN.
Main Function:

Displays a menu for user operations.
Prompts the user to enter their PIN and validate it.
Performs the selected operation (balance inquiry, withdrawal, or PIN reset).
Handles exceptions for incorrect PINs, insufficient balance, and PIN confirmation failures.
Validation Functions:

validate_pin(mypin, pin): Checks if the provided PIN matches the stored PIN.
check_balance(balance, amount): Ensures that the withdrawal amount does not exceed the current balance.
check_pin(new_pin, confirm_pin): Verifies that the new PIN and its confirmation match.
Example Usage
Balance Inquiry:

Select option 1.
Enter the correct PIN.
The current balance will be displayed.
Withdraw Amount:

Select option 2.
Enter the correct PIN.
Specify the amount to withdraw.
The system will display the remaining balance or an error if the balance is insufficient.
Reset PIN:

Select option 3.
Enter and confirm the new PIN.
The PIN will be updated if the confirmation matches.
Cancel Transaction:

Select option 4.
The transaction will be canceled, and the system will exit.
