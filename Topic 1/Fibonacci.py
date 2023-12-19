def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

user_input = int(input("Enter the position of the Fibonacci number: "))
result = fibonacci(user_input)
print(f"The {user_input}th Fibonacci number is: {result}")
