def add(num1,num2):
    print(num1+num2)
    return
def sub(num1,num2):
    print(num1-num2)
    return
def mul(num1,num2):
    print(num1*num2)
    return
def div(num1,num2):
    print(num1/num2)
    return
def mod(num1,num2):
    print(num1%num2)       
    return
def pow(num1,num2):
    print(num1**num2)       
    return
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Power")
num1=int(input())
num2=int(input())
choice=int(input())
if choice==1:
    add(num1,num2)
if choice==2:
    sub(num1,num2)
if choice==3:
    mul(num1,num2)
if choice==4:
    div(num1,num2)
if choice==5:
    mod(num1,num2)
if choice==6:
    pow(num1,num2)
