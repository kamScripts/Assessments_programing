from input_module import take__num
from processing import Calculator
from output_module import output_calc
from files import append_to_file

calc_path = 'calculations.txt'
calc = Calculator()



def app():
    num1 = take__num('frist')
    num2 = take__num('second')
    calculation = [
                    calc.add(num1, num2),
                    calc.subtract(num1, num2),
                    calc.multiply(num1, num2),
                    calc.divide(num1, num2)]
    
    for item in calculation:
        output = output_calc(num1, num2, item[1], item[0])
        print(output)
        append_to_file(calc_path, output)


app()