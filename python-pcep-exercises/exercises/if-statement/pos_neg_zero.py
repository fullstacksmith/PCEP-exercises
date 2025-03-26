#Positive, Negative, or Zero
#Write a program that asks the user for a number and determines whether it is positive, negative, or zero.

intNumber = int(input('Type a number please: '))

if intNumber < 0:
    print('Negative number' + str(intNumber))
if intNumber > 0:
    print('Positive number ' + str(intNumber))
if intNumber == 0:
    print('Zero' + str(intNumber))

