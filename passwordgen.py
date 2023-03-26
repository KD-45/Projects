import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers=['1','2','3','5','4']
symbol=['!','@','#','$','%']
print("welcome to password generator\n")
nr_letters=int(input("enter the number of letters"))
nr_numbers=int(input("enter the number of numbers"))
nr_symbols=int(input("enter the number of symbols"))
password_list=[]
for char in range(1,nr_letters+1):
    password_list+=random.choice(letters)
for char in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)
for char in range(1,nr_symbols+1):
    password_list+=random.choice(symbol)
print(password_list)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f"your generated password is {password}")