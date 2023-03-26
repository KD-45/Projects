print("welcome to treasure island")
first_choice=input("left or right")
if first_choice=="left":
    print("you passed the first level")
    sec_choice=input("wait or swim")
    if sec_choice=="wait":
        print("passed 2nd level")
        third_choice=input("choose door red or white")
        if third_choice=="white":
            print("you have found the treasure")
        else:
            print("game over at third level")
    else :
        print("game over at 2nd level")
else :
    print("Game over at first level you fucking nooooob")