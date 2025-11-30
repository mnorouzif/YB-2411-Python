class MathSeries:
    # @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)



    # @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2))


if __name__ == "__main__":
    n = 5

    print("Factorial (recursive):", MathSeries.factorial_recursive(n))
    print("Fibonacci (recursive):", MathSeries.fibonacci_recursive(n))
