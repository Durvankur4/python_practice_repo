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

for i in range(1,10):
    if i == 1:
        print(f"{i}st")
    elif i == 2 :
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")