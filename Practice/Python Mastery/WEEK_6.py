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

# class BankAccount :

#     def __init__(self,owner : str ,balance : float):
#         self.owner = owner
#         self._balance = balance
    
#     @property
#     def balance(self):
#         return self._balance
     
#     def deposite(self, amt : float):
#         if amt < 0 :
#             raise ValueError("not enough funds")
#         self._balance += amt
#         print(f"credited {amt} to {self.owner}'s account")
#         return self.balance
    
#     def withdraw(self, amt : float):
#         if amt < 0 : 
#             raise ValueError("not enough funds")
#         elif amt > self._balance:
#             print("not enough balance")
#         self._balance -= amt
#         print(f"debited {amt} from {self.owner}'s account")
#         return self._balance

# acc1 = BankAccount("mark",10000)
# print(acc1.balance)
# print(acc1.deposite(5000))
# print(acc1.withdraw(10000))

# Problem 2 (Medium) — Inheritance vs Composition
# Make a small game-style example:
# Character → base class
# name
# hp
# attack() method
# Mage(Character) → child
# additional attribute mana
# special attack consuming mana
# Topics required
# Inheritance
# Method overriding
# Calling parent methods (super())


# """
# created a game of duel between characters below 
# """

# class Character():
#     def __init__(self,name : str, hp : int):
#         self.name = name
#         self.hp = hp

#     def attack (self, target):
#         target.hp -= 10
    
# class Mage(Character) :
#     def __init__(self, name , hp , mana : int):
#         super().__init__(name, hp)
#         self.mana = mana

#     def special(self, target):
#         if self.mana < 10 :
#             print("Not enough Mana")
#             self.attack(target)
#         else:
#             self.mana -= 10
#             target.hp -= 20

# Soldier = Character("Knight", 150)
# Wizzard = Mage("Gnadalf", 120, 50)

# print(f"{Soldier.name}, {Soldier.hp} hp")
# print(f"{Wizzard.name}, {Wizzard.hp} hp")
# print("Fight begin :")

# while Soldier.hp > 0 and Wizzard.hp > 0 :
#     print(f"\nSoldier {Soldier.hp}")
#     print(f"Wizzard {Wizzard.hp}")
#     Soldier.attack(Wizzard)
#     Wizzard.special(Soldier)
#     if Soldier.hp <= 0 or Wizzard.hp <= 0:
#         if Wizzard.hp == 0: 
#             print("\nwizz died")
#         if Soldier.hp == 0: 
#             print("\nsoldier died")
#         break

# print("\nFinal")
# print(f"{Soldier.name}, {Soldier.hp} hp")
# print(f"{Wizzard.name}, {Wizzard.hp} hp")