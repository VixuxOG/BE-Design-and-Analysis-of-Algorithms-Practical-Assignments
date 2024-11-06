def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth number.
    
    Parameters:
    n (int): The number of Fibonacci numbers to generate.
    
    Returns:
    list: The Fibonacci sequence up to the nth number.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

# Get user input for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))
