def take__num(order):
    num = input(f'input the {order} number: ')
    if num.isdecimal():
        return float(num)
    else:
        print('it need to be a number')
def split_input():
    eq = input('input the equation: ')
    splited_string = eq.split(' ')
    
