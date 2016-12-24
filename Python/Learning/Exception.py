while True:
    print('Enter First Number')
    num1=float(input())
    print('Enter Second Number')
    num2=float(input())
    num3=num1/num2
    if(num1==0 or num2==0):
        break
    print("The result is " + num3)
    
    