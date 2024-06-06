def gcd_number(a,b):
    if b==0:
        return a
    else :
        return gcd_number(b , a % b )
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
print(f'GCD = {gcd_number(num1,num2)}')
