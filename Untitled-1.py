def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        return None  # Handle negative input
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
print("Hello world");
print(factorial(8));