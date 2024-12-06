from input_module import take__num
from processing import Calculator
from output_module import output_calc


calc = Calculator()
num1 = take__num('frist')
num2 = take__num('second')
addition = calc.add(num1, num2)
subtraction = calc.subtract(num1, num2)


print(output_calc(num1, num2, addition[1], addition[0]))
