def is_armstrong(number):
    if number == 0:
        return 0
    else:
        return (number % 10) ** len(str(number)) + is_armstrong(number // 10)
def armstrong(number):
    return number == is_armstrong(number)
num = int(input("Enter the number :"))
if armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    
        
