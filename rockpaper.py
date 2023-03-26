import random
print("enter 0 for rock 1 for paper and 2 for scissors ")
list_choice=["rock", "paper", "scissor"]
computer_num=random.randint(0,2)
user_num=input("enter your choice number for the game")
if user_num== "0":
    if computer_num=="0":
        print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} so its draw  ")
    elif computer_num=="1":
        print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} so computer won")
    else :
         print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} so you  won")
elif user_num=="1":
    if computer_num=="0":
        print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} you won")
    elif computer_num=="1":
        print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} so its draw")
    else :
         print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} so computer won")
elif user_num=="2":
    if computer_num=="0":
        print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} computer won")
    elif computer_num=="1":
        print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} so you won")
    else :
         print(f"your choice is {list_choice[int(user_num)]} and computer choice is {list_choice[int(computer_num)]} so its draw")
else :
    print("invalid choice made")
