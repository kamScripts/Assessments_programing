
eq_sign = {'-': 'difference between', '+' : 'sum of', '*': 'product of', '/': 'quotient of'} 


def output_calc(num1, num2, sign, result):
    output = f'The {eq_sign.get(sign)} {num1} and {num2} is {result}'
    return output


