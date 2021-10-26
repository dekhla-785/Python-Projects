num = int(input("Enter your number to divide: "))

divisorList = list(range(1,num+1))

dividend = []

for number in divisorList:
    if num%number == 0:
        dividend.append(number)

print(dividend)