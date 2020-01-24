# So User can choose which times tables they want.
print("Welcome to Maths Quest! ", end = '')
name = input('What is your name? ')
print(name, "which times table would you like to practice? ", end = "")
num = int(input("Please enter a number between(1 - 12): "))

while num not in range(13):
    num = int(input("(1 - 12): "))
else:
    pass
# Letting user know what there next step is.
print("Ok " + name, "on a piece of paper, write down the " + str(num)  + " times table from 1 to 12.")
print("When you're ready I'll show you the answer so you can check your work.")
# Asking if user is ready to run Program
userinput = 'y'
userinput = 'n'
# Asking if user is Ready.
userinput = input("Are you Ready y/n: ")
# If y first print times tables
for (userinput == 'y'):
        for i in range(1, 13):
           print(num, 'x', i, '=', num*i)
# If n loop back till user choose y
while (userinput == 'n'):
    userinput = input("Are you Ready y/n: ")
else (userinput == 'y'):
    for i in range(1, 13):
       print(num, 'x', i, '=', num*i)

# End of Program
user = input("Did you get them all right y/n: ")
if (user == 'y'):
 print('Great Job! Thank you for playing Math Quest.')
if (user == 'n'):
    print('Better luck next time.')
