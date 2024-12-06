class Calculator():
    def add(self, *args):
        result=0
        for arg in args:
            result+=arg
        return (result, '+')
    def subtract(self, *args):
        result=0
        for arg in args:
            result-=arg
        return (result, '-')
    def multiply(self, *args):
        result=0
        for arg in args:
            result*=arg
        return (result, '*')
    def divide(self, *args):
        result=0
        for arg in args:
            result/=arg
        return (result, '/')
    
    