import math 
from tabulate import tabulate



print ( '\033[1m' + '---------- Welcome to calculator ----------' + '\033[0m')

print("To start Enter a mode you need:")


counter= 0
while True:
    info = {'option': ['Basic', 'Advance'] ,'Your choice:': ['1', '2'] }
    print(tabulate(info, headers='keys', tablefmt='fancy_grid') )
    choice = int(input("we waiting for you .. :"))


    if choice == 1 :

        operation = input('''
        Please type in the math operation you would like to complete:
        1-+ for addition
        2-- for subtraction
        3-* for multiplication
        4-/ for division
        5-** for Exponential
        6-// for Floor Division
        ''')

        number_1 = float(input('Enter your first number: '))
        number_2 = float(input('Enter your second number: '))

        if operation == '+' or operation == 'jam' or operation == 'be alave':
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)
            counter+=1

        elif operation == '-' or operation == 'menha' or operation == 'tafrigh':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)
            counter+=1

        elif operation == '*'  or operation == 'zarb':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)
            counter+=1

        elif operation == '**'  or  operation == 'tavan': 
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 ** number_2)
            counter+=1

        elif operation == '/' or  operation == 'taqsim' or operation == 'taghsim':
            if number_2 == 0.0:
                print("Divide by 0 Error")
            else :
                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)
            counter+=1

        elif operation == '//' or operation == 'taghsim sahih':
            if number_2 == 0.0:
                print("Divide by 0 Error")
            else :
                print('{} // {} = '.format(number_1, number_2))
                print(number_1 / number_2)
            counter+=1    

        else:
            print('You have not typed a valid operator, please run the program again.')

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "yes":
            continue
        change_mode =  input("do you want to change your mode to advance? (yes/no): ")
        if change_mode != "yes":
            break


    if choice == 2 :
    
        operation = input('''
        Please type in the math operation you would like to complete:
        -sin for addition
        -cos for subtraction
        -tan for multiplication
        -abs for dabsolute-value
        -radical for square root
        -Pr for Prime number
        -x! for factorial 
        -a  for Decimal to Hexadecimal 
        -b  for Decimal to Octal
        -c  for Decimal to Binary
        ''')

        number_1 = float(input('Enter your number: '))
        # number_2 = float(input('Enter your second number: '))

        if operation == 'sin':
            print('sin({}) = '.format(number_1))
            print( math.sin(number_1) )
            counter+=1

        elif operation == 'cos':
            print('cos({}) = '.format(number_1))
            print(math.cos(number_1))
            counter+=1

        elif operation == 'tan':
            print('tan({}) = '.format(number_1))
            print(math.tan(number_1))
            counter+=1

        elif operation == 'abs':
            abs_number_1 = abs(number_1)
            print('|',number_1, '| = ')
            print(abs_number_1, sep='')
            counter+=1

        elif operation == 'radical':
            if number_1 <0:
                print("Math domain Error")
            else :
                print('(√{}) = '.format(number_1))
                print(math.sqrt(number_1))
            counter+=1

        elif operation == 'prime number' or operation == 'pr':
            if number_1 > 1:
                # Iterate from 2 to n / 2
                for i in range(2, int(number_1/2)+1):
                    # If num is divisible by any number between
                     # 2 and n / 2, it is not prime
                 if (number_1 % i) == 0:
                    print(number_1, "is not a prime number")
                    break
                else:
                    print(number_1, "is a prime number")
            else:
                 print(number_1, "is not a prime number")
            counter+=1


        elif operation == 'x!' or operation == 'factorial':
            fact = 1
  
            for i in range(1,int(number_1)+1):
                 fact = fact * i
      
            print ("The factorial of "+str(int(number_1))+" is : ",end="")
            print (fact)
            counter+=1

        elif operation =='a':
            print("Hexadecimal form of " + str(number_1) +
                    " is " + hex(int(number_1)).lstrip("0x").rstrip("L"))
            counter+=1

        elif operation == 'b':
            print("Octal form of " + str(number_1) +
                 " is " + oct(int(number_1)).lstrip("0o").rstrip("L"))
            counter+=1

        elif operation == 'c':
            print("Binary form of " + str(number_1) +
             " is "+bin(int(number_1)).lstrip("0b").rstrip("L"))
            counter+=1


        else:
            print('You have not typed a valid operator, please run the program again.')


        print("Number of times you used the calculator is" , counter)

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "yes":
            continue
    change_mode =  input("do you want to change your mode to advance? (yes/no): ")
    if change_mode != "yes":
            break






