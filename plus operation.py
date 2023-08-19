def addition(num1,num2):
    output=num1+num2
    return output


def calculate(num1,num2,operation):
    if operation=="+":
        print(addition(num1,num2))
        
    




num1=int(input("Enter the first number here young master :) :"))
num2=int(input("Enter the second number here young master :) :"))    
operation=input("Enter the sign u wish to use on the previous numbers young master :) :")
calculate(num1,num2,operation)