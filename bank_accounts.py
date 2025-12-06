class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"Acount {self.name} created.\nBalance=$'{self.balance:.2f}'")

    def getBalance(self):
        print(f"\nAccount {self.name} has ${self.balance:.2f}")

    def debosit(self, amount):
        self.balance += amount
        print("\nDeposit Complete:")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"sorry, account '{self.name}' only has a balance of {self.balance:.2f}"
            )

    def withDraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nwithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer..🚀")
            self.viableTransaction(amount)
            self.withDraw(amount)
            account.debosit(amount)
            print("\nTransfer Complete \n\n********** ")
        except BalanceException as error:
            print(f"\nTransfer Interrupted ❌ {error}")


class InterestsRewardAccount(BankAccount):
    def debosit(self, amount):
        self.balance += amount * 1.05
        print("\ndeposit complete")
        self.getBalance()
        
class savingsAccount(InterestsRewardAccount):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5
        
    def withDraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\n withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraaw Interrupted: {error}')