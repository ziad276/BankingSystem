from bank_accounts import *

ziad = BankAccount(120.345, "ziad")

gouhar = BankAccount(330, "gouhar")

ziad.getBalance()

ziad.debosit(100)

ziad.withDraw(0)

ziad.transfer(2020, gouhar)

zzzziad = InterestsRewardAccount(1000000, "zoz")

zzzziad.getBalance()
zzzziad.debosit(100)
zzzziad.transfer(100, gouhar)

blaze = savingsAccount(1000, "blaze")

blaze.getBalance()

blaze.debosit(100)

blaze.transfer(100, gouhar)