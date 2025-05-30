class FactorialCalculator:
    @staticmethod #???
    def calculate(number):
        if number == 0 or number == 1:
            return 1
        result = 1
        for i in range(2, number + 1, 1 ):
            result *= i
        return result

# =============
n = int(input("Enter a number to calculate its factorial: "))
calculator = FactorialCalculator()
print(f"The factorial of {n} is {calculator.calculate(n)}")
