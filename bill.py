import random
name_string=input("give me all the names, separated by comma")
names=name_string.split(", ")
num_items=len(names)
random_choice=random.randint(0,num_items-1)
person_pay=names[random_choice]
print(f"{person_pay} is going to pay")
