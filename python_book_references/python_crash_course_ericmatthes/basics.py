# print("hello world")

# message = "hello"
# print(message)
# message = "woeld"
# print(message)

# name = "eric"
# print(f"hello {name.upper()}, hows your day")
# famous = " \talbert einstein\n"

# print(f'{famous.lstrip()} oce said, "an apple a day keeps doctor away"')

# print(0.2 + 0.1)
# import this

# mortorcycles = ["honda","yamaha"]
# print(mortorcycles)
# mortorcycles[0] ="ducati"
# print(mortorcycles)
# del mortorcycles[1]
# print(mortorcycles)

# invite_list = ["ana","bell","theo"]
# print(f"invite {invite_list[0]}, {invite_list[1]} ,{invite_list[2]} to dinner")
# print(f"{invite_list[1]} cannot join")
# invite_list[1] = "man"
# print(f"invite {invite_list[0]}, {invite_list[1]} ,{invite_list[2]} to dinner")
 
# print("i found bigger table")
# invite_list.insert(1,"gian")
# invite_list.insert(0,"thian")
# invite_list.append("michan")
# print(f"invite {invite_list[0]}, {invite_list[1]} ,{invite_list[2]} , {invite_list[3]}, {invite_list[4]}, {invite_list[5]} to dinner")

# print(f"{invite_list.pop()} sorry you are not invited")
# print(f"{invite_list.pop()} sorry you are not invited")
# print(f"{invite_list.pop()} sorry you are not invited")
# print(f"{invite_list.pop()} sorry you are not invited")
# print(invite_list)
# print(f"{invite_list[0]}  you are  invited")
# print(f"{invite_list[1]}  you are  invited")
# print(invite_list)

# cars = ["toyota","subaru","bmv"]
# print("herers the ori list")
# print(cars)

# print("herers the sorted list")
# print(sorted(cars))

# print("herers the ori list")
# print(cars)

# cars.sort(reverse=True)
# print(cars)


# pizzas = ["peperoni","pinnaple","margarita"]

# for pizza in pizzas :
#     print(f"i love {pizza} pizza")
# print("i really love pizzas")

# print([x**3 for  x in range(11)])

# list = ['a','b','c','d','e']
# print(list[-3:])

# points : int = 0
# alien_color = ['green','yellow','red']
# alien_color_selection = 'red'
# if alien_color_selection == 'green':
#     print("player earned 5 points for sooting alien")
# elif alien_color_selection == 'yellow':
#     print("player earned 10 points for shooting alien")
# elif alien_color_selection == 'red':
#     print("player earned 15 points for shooting alien")


# current_users = ['ana','john','admin','jenna','rob']
# new_users = ['ana','theo','mark','raj','kendal',"John"]
# current_users_lower = current_users[:]
# if current_users == []:
#         print("we need to find some users")
# for user in current_users :
#     if user == "admin":
#         print(f"hello admin")
#     else:
#         print(f'hello there thanks for login again {user}')
#     current_users_lower.append(user.lower)

# for n_user in new_users:
#     if n_user.lower() in current_users_lower:
#           print("name alredy exist pick different name")
#     else :
#          print("yoycan take that username")

# for i in range(1,10):
#     if i == 1:
#         print(f"{i}st")
#     elif i == 2 :
#         print(f"{i}nd")
#     elif i == 3:
#         print(f"{i}rd")
#     else:
#         print(f"{i}th")

# persons = [
#     {
#     "f_name": "Amanda",
#     "l_name": "Greg",
#     "city": "Huston"},
#     {
#     "f_name": "Rob",
#     "l_name": "Thomas",
#     "city": "Burgandy"}
#     ]

# for person in persons :
#     print(f"\nhi {person["f_name"]} {person["l_name"]} from {person['city']}")

# prompt = "\n Tell me something, and i will repeat it back to you : "
# prompt += "\n Enter 'quit' to end the programme."
# message = "" 
# while message != "quit":
#     message = input("enter the message :")

#     if message != "quit":
#         print(message)

# prompt = "\n(enter quit to stop adding toppings)"
# prompt += "Enter the toppings on your pizza :"


# active = True
# while active:
#     print(prompt)
#     toppings = input()
#     if toppings == 'quit':
#         active = False
#     else :
#         print(f"we'll add {toppings} to your pizza.")

# unconfirmend_users = ["alice","brian","candice"]
# confirmed_users = []

# while unconfirmend_users :
#     curr_user = unconfirmend_users.pop()
#     print(f"Verifying Current user : {curr_user}")
#     confirmed_users.append(curr_user)
#     print("user verified")

# print("\nthe following users have been verified :")
# for user in confirmed_users:
#     print(user.title())

# pets = ["dogs","cats","rats","dogs","goldfish","cats","rats","dogs","cats","rats"]
# print(pets)
# while "cats" in pets:
#     pets.remove('cats')
# print(pets)


# responses= {}
# polling_active = True
# while polling_active :
#     name = input("enter the persons name : ")
#     response = input("enter your favourite place : ")

#     responses[name] = response
    
#     repeat = input("would you like to let other person respond : (yes/no)").lower()
#     if repeat == "no":
#         polling_active = False

# print("Polling Reults ")
# for name,response in responses.items():
#     print(f"{name} : {response}")

# sandwitch_orders = ["cheeze sandwitch","fruit sandwitch","shezwan sandwitch"]
# finished_sandwitch = []

# print(sandwitch_orders)
# while sandwitch_orders:
#     finished_sandwitch.append(sandwitch_orders.pop())
    
# print(finished_sandwitch)

# list_msg = ["hi", "hello", "hui"]
# sent_messages = []

# def send_messages(messages):
#     for item in messages:
#         print(item)
#         sent_messages.append(item)

# print(list_msg)
# send_messages(list_msg[:])   
# print(sent_messages)
# print(list_msg)

# def make_pizza(size,*toppings):
#     '''print the list of toppings that have been requested'''

#     print(f"\nmaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16,'peporoni')
# make_pizza(18,'mushroom','green pepers','cheeze')

# def build_profile(first,last,**user_info):
#     '''build dictionary of users info'''
#     user_info['first-name'] = first
#     user_info['last-name'] =last
#     return user_info

# user_profile = build_profile('albert','einstein',location = 'priston')
# print(user_profile)

# classes

# class Dog:
#     '''simple dog class'''
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     #these are methods and they are no diff than a function 
#     def sit(self):
#         print(f"{self.name} is now sitting")
#     def roll_over(self):
#         print(f"{self.name}is now rolling over.")
    
# my_dog = Dog('willie',6) #here my_dog is an instance of a Class and Dog is a Class
# print(f'my dogs name is {my_dog.name} and his age is {my_dog.age}')
# my_dog.sit()
# my_dog.roll_over()

# class Restaurant:
#     def __init__(self,restaurant_name,cusine_type):
#         self.restaurant_name = restaurant_name
#         self.cusine_type = cusine_type

#     def describe_restaurant(self):
#         print(f"\nWelcome to {self.restaurant_name} restaurant.")
#         print(f"We serve {self.cusine_type} Cusine.")
#         return ""

#     def open_restaurant(self):
#         print("This Restauant is now open!")
#         return ""

# rest_1 = Restaurant("Panjabi Dhaaba","Indian")
# rest_2 = Restaurant("Chiese Tok","Chinese")
# rest_3 = Restaurant("Italian Diner","Italian")

# list_rest = [rest_1,rest_2,rest_3]
# for item in list_rest:
#     print(item.describe_restaurant())
#     print(item.open_restaurant())

# class User:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()

#     def describe_user(self):
#         print(f"\nMy name is {self.first_name} {self.last_name}")
     
#     def greet_user(self):
#         print(f"Hello {self.first_name}! nice to meet you!")

# user_1 = User("aman","bera")
# user_2 = User("sia","rahtod")
# user_3 = User("tia","kumar")
# list_user = [user_1,user_2,user_3]
# for user in list_user:
#     user.describe_user()
#     user.greet_user()

# class Restaurant:
#     def __init__(self,restaurant_name,cusine_type,numbers_served = 0):
#         self.restaurant_name = restaurant_name
#         self.cusine_type = cusine_type
#         self.numbers_served = numbers_served 

#     def describe_restaurant(self):
#         print(f"\nWelcome to {self.restaurant_name} restaurant.")
#         print(f"We serve {self.cusine_type} Cusine.")
        

#     def open_restaurant(self):
#         print("This Restauant is now open!")
        
#     def set_number_served(self,served_people):
#         self.numbers_served += served_people
#         print(f"this restaurant has served {self.numbers_served} people.")
        


# rest_1 = Restaurant("Panjabi Dhaaba","Indian",20)
# # rest_2 = Restaurant("Chiese Tok","Chinese",50)
# # rest_3 = Restaurant("Italian Diner","Italian",40)
# rest_1.set_number_served(30)


# class User:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.login_attempt = 0

#     def describe_user(self):
#         print(f"\nMy name is {self.first_name} {self.last_name}")
     
#     def greet_user(self):
#         print(f"Hello {self.first_name}! nice to meet you!")
    
#     def increment_login_attempt(self):
#         self.login_attempt += 1 
#         print(f"login attempted {self.login_attempt} times.")

#     def reset_login_attempts(self):
#         self.login_attempt = 0
#         print(f"login attempted {self.login_attempt} times.")

# user_1 = User("aman","bera")

# user_1.increment_login_attempt()
# user_1.increment_login_attempt()
# user_1.increment_login_attempt()
# user_1.increment_login_attempt()
# user_1.reset_login_attempts()
# user_1.increment_login_attempt()
# from random import randint
# class Die:
#     def __init__(self,sides = 6):
#         self.sides = sides
#         print(f"this die is {self.sides} sided")

#     def roll_die(self):
#         value = randint(1,self.sides)
#         print(f"the die rolled {value}")

# # my_die = Die(20)
# # for i in range(11):
# #     my_die.roll_die()

# lottery_number = (1,3,'a','b')
# winning_number = (1,'a','b',3)
# from random import randint
# count = 0 

# while True:
#     count +=1
#     my_ticket = []

#     for i in range(len(winning_number)):
#         '''this will generate a random ticket form the lottey_number of size winnig_numebr'''

#         index_random = randint(0,len(lottery_number)-1)
#         my_ticket.append(lottery_number[index_random])

#     print(my_ticket)
#     if my_ticket == winning_number:
#         break
#     if count == 1_000_000 :
#         print("its taking too long")
#         break
# print(f"you won after {count} number of tries")

# with open("D:/03_Code\python\python_book_references\python_crash_course_ericmatthes\pi_digits.txt") as file_obj : #absolute pathing
#     lines = file_obj.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))

# user_name = input("enter your name : ")
# with open("guests.txt",'a') as file_obj:
#     file_obj.writelines(user_name)

# print("give me two numebrs, and i'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst: number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Enter Second number: ")
#     if first_number == 'q':
#         break

#     try:
#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("cant divide by zero hero")
#     else:
#         print(answer)

# import json
# numbers = [2,3,5,7,11,13]
# file_name = 'numbers.json'
# with open(file_name,'w') as f :
#     json.dump(numbers,f)

# import json 
# file_name = 'numbers.json'
# with open(file_name) as f:
#     numbers = json.load(f)

# print(numbers)

import json 

def greet_user():
    '''Greet the user by name.'''
    file_name = 'username.json'
    try :
        with open(file_name) as f :
            username = json.load(f)
    except FileNotFoundError :
        username = input("waht is your name : ")
        with open(file_name,'w') as f :
            json.dump(username,f) 
            print(f"we'll remember you when you come back {username}")
    else:
        print(f"Welcome back {username}")
        
greet_user()


def get_stored_username():
    '''get sored username if available.'''
    file_name = 'username.json'
    try :
        with open(file_name) as f :
            username = json.load(f)
    except FileNotFoundError :
        return None
    else:
        return username
    
def greet_user():
    username = get_stored_username()
    if username:
        print(f"welcome back {username}")
    else:
        file_name = 'username.json'
        username = input("waht is your name : ")
        with open(file_name,'w') as f :
            json.dump(username,f) 
            print(f"we'll remember you when you come back {username}")