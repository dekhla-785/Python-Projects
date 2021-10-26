# def add(num,num_2):
#     print("Sum of two numbers is: ",num+num_2)

# def sub(num,num_2):
#     print("Subraction of two numbers is: ",num-num_2)

# def mul(num,num_2):
#     print("Multiplication of two numbers is: ",num*num_2)

# def div(num,num_2):
#     print("Division of 2 numbers is: ",num/num_2)

# num = int(input("Enter your first number: "))
# num_2 = int(input("Enter your second number: "))


# a = add(num,num_2)
# s = sub(num,num_2)
# m = mul(num,num_2)
# d = div(num,num_2)

# OR 

select = [1,2,3,4]
print(select)
user_select = int(input("Select your number for Calcultion: "))
while(user_select!=select):
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    if user_select==1 in select:
        print("Summ of two numbers is:",num1+num2)
        break
    elif user_select==2 in select:
        print("Subraction of 2 numbers is: ",num1-num2)
        break
    elif user_select==3 in select:
        print("Multiplication of two numbers is: ",num1*num2)
        break
    elif user_select==4 in select:
        print("Division of two numbers is: ",num1/num2)
        break
    else:
        if user_select not in select:
            print("You have selected invalid number, Please select another number from list")
        break