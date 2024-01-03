class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("cannot divide by zero")
calculator=Calculator()
result=calculator.add(40,2)
print(result)

# instance(object)method
# class method
        

