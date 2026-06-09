from bank_account import *
peeran=Bankaccount(2000,"Peeran")
yash=Bankaccount(5000,"Yash")

peeran.getbalance()
yash.getbalance()

peeran.deposit(500)
yash.deposit(1000)

yash.withdraw(10000)
yash.withdraw(200)

peeran.transfer(100,yash)

jim=intrestrewardacct(1000,"Jim")

jim.getbalance()

jim.deposit(100)

jim.transfer(50,peeran)

blaze=savingsacct(500,"Blaze")
blaze.getbalance()
blaze.deposit(100)
blaze.withdraw(50)