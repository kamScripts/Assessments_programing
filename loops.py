num = abs(int(input("Type the number ")))


def factorial(number):
    fact = number    
    for i in range(number, 1, -1):
        fact*=(i-1)
    print(f'{number}:{fact}')
        
        
factorial(num)
        
        
            