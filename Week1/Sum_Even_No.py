def Sum_even_No(n):
    even_sum = 0

    # Loop from 1 to n
    for i in range(1, n + 1):
        if i % 2 == 0:      
            even_sum += i

    # Print the result
    print("The sum of even numbers from 1 to", n, "is", even_sum)

if __name__ == "__main__":
    
    n = int(input("Enter a positive number: "))
    
    Sum_even_No(n)