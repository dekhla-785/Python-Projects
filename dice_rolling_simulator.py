import random
dice = [1,2,3,4,5,6]
show = random.choice(dice)

#OR

# show = random.randint(1,6)
# print(show)

if show == 1:
    print(" **  ")
    print("* *")
    print("  * ")
    print("  * ")
    print("*****")
elif show ==2:
    print("****   ")
    print("   #")
    print("**** ")
    print("#   ")
    print("****   ")
elif show ==3:
    print(" *****   ")
    print("     #")
    print("  ****")
    print("     #")
    print(" ***** ")
elif show ==4:
    print("*    ")
    print("*   *")
    print("*****    ")
    print("    *")
    print("    *")
elif show==5:
    print("*****")
    print("#    ")
    print("*****    ")
    print("    # ")
    print("*****    ")
elif show==6:
    print("*****    ")
    print("#    ")
    print("*****   ")
    print("#   #")
    print("*****   ")
else:
    pass



