class Atm:
    def __init__(self, cardNumber, pinNimber):
        self.cardnumber = cardNumber
        self.pinNimber = pinNimber

    def checkBalance(self):
        print("Your current balance is $1000000")

    def withdraw(self, amount):
        balance = 1000000 - amount
        print("You have withdrawn $" + str(amount) + ". Your balance is now $"+ str(balance))
    
    def deposit(slef, amount):
        balance = 1000000 + amount
        print("You have deposited $" + str(amount) + ". Your balance is now $" + str(balance))


def function():
    card_number = input("Your card number (10 digits): ")
    pin_number  = input("Your pin number (3 digits): ")

    thing =  Atm(card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl   3.Deposit")
    activity = int(input("enter activity number: "))

    if (activity == 1):
        thing.checkBalance()
    elif (activity == 2):
        amount = int(input("How much would you like to withdraw? "))
        thing.withdraw(amount)
    elif (activity == 3):
        amount = int(input("How much would you like to deposit? "))
        thing.deposit(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    function()
