class BalanceException(Exception):
    pass
class Bankaccount:
    def __init__(self,initialamount,accountname):
        self.balance = initialamount
        self.accountname = accountname

        print(f"\n Account '{self.accountname}' created.\n Balance =$'{self.balance:.2f}'")


    def getbalance(self):
        print(f"\n Account '{self.accountname}' balance is ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"\n Amount ${amount:.2f} deposited into account '{self.accountname}'.")
        self.getbalance()

    def viableTransaction(self,amount):

        if self.balance >= amount:
            return

        else:
            raise BalanceException(
                f"\n Sorry ,account '{self.accountname}' has insufficient balance of ${self.balance:.2f} for this transaction."
            )    
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print(f"\n Withdraw Complete.")
            self.getbalance()  
        except BalanceException as error:
            print(error)  

    def transfer(self,amount,account):
        try:
            print('\n ***********\n\nBeggining transfer process...🚀🚀🚀')   
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\n Transfer Complete.")

        except BalanceException as error:
            print(f"\n Transfer interupted .❌❌")     
                     


class intrestrewardacct(Bankaccount):
    def deposit(self,amount):
        self.balance=self.balance+amount*(1.05)

        print("\n Deposit Complete")
        self.getbalance()                     



class savingsacct(intrestrewardacct):
    def __init__(self,initialamount,acctname):
        super().__init__(initialamount,acctname)
        self.fee=5

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\n Withdraw Complete.")
            self.getbalance()
        except BalanceException as error:
            print(f"\n Withdraw interupted .❌❌")