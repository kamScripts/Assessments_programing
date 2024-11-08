def temp_converter():
    conversion_type = input("Choose convertion type 1 for celsius to fahrenheit, type 2 for fahrenheit to celsius ")
    sign = ""
    temp = int(input('temperature value '))
    if conversion_type == '1':
        sign = "°C"
        temp = (temp * (9/5)) +32
        print(temp, sign)
    elif conversion_type == '2':
        sign = "°F"
        temp = (temp - 32) * (5/9)
        print(temp, sign)
    else:
        print("You typed something wrong!")
        
temp_converter()