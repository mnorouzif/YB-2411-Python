# def fact (n):

number = input("input value(PLEASE PUT INTENGER NUMBER):")

n = float(number)
n = round(n)
def factorial(n):
    if n < 0:
        return "Unidentify number lower than zero"

    elif 0 < n <= 1:
        return 1

    else:
        result = 1
        for i in range(1, n + 1):
            print(", ",i)    
            result *= i
        return result

print(factorial(n))
