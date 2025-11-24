# Problem 1 (Easy) — Simple Class with Methods
# Create a class BankAccount with:
# .deposit(amount)
# .withdraw(amount)
# .balance property (read-only)
# Proper error handlin
# Topics required
# Constructor (__init__)
# Instance attributes
# Input validation

class BankAccount :

    def __init__(self,owner : str ,balance : float):
        self.owner = owner
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
     
    def deposite(self, amt : float):
        if amt < 0 :
            raise ValueError("not enough funds")
        self._balance += amt
        print(f"credited {amt} to {self.owner}'s account")
        return self.balance
    
    def withdraw(self, amt : float):
        if amt < 0 : 
            raise ValueError("not enough funds")
        elif amt > self._balance:
            print("not enough balance")
        self._balance -= amt
        print(f"debited {amt} from {self.owner}'s account")
        return self._balance

acc1 = BankAccount("mark",10000)
print(acc1.balance)
print(acc1.deposite(5000))
print(acc1.withdraw(10000))