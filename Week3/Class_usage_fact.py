class FactorialCalculator:
    def __init__(self, number):
        self.number = number
        
    def calculate(self):
        if self.number == 0 or self.number == 1:
            return 1
        result = 1
        for i in range(2, self.number + 1, 1):
            result *= i
        return result

# =============
n = int(input("Enter a number to calculate its factorial: "))
calculator = FactorialCalculator(n)
print(f"The factorial of {n} is {calculator.calculate()}")
