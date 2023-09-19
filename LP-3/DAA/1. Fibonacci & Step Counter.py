# Write a program to calculate Fibonacci numbers and find its step count
# Author: Kedar Koshti (41435)

# Function to calculate Fibonacci number using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to calculate Fibonacci number using iteration (dynamic programming)
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Function to count the number of steps needed to calculate a Fibonacci number using recursion
def count_steps_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 + count_steps_recursive(n - 1) + count_steps_recursive(n - 2)

# Function to count the number of steps needed to calculate a Fibonacci number using iteration
def count_steps_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    steps = [0] * (n + 1)
    steps[1] = 1

    for i in range(2, n + 1):
        steps[i] = 1 + steps[i - 1] + steps[i - 2]

    return steps[n]

# Input the desired Fibonacci number 'n'
n = int(input("Enter the value of n: "))

# Calculate and print the Fibonacci number using recursion
fib_recursive = fibonacci_recursive(n)
print(f"Fibonacci number (Recursive) for n = {n}: {fib_recursive}")

# Calculate and print the number of steps needed using recursion
steps_recursive = count_steps_recursive(n)
print(f"Number of steps (Recursive) to calculate Fibonacci number for n = {n}: {steps_recursive}")

# Calculate and print the Fibonacci number using iteration
fib_iterative = fibonacci_iterative(n)
print(f"Fibonacci number (Iterative) for n = {n}: {fib_iterative}")

# Calculate and print the number of steps needed using iteration
steps_iterative = count_steps_iterative(n)
print(f"Number of steps (Iterative) to calculate Fibonacci number for n = {n}: {steps_iterative}")

def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    
    fibonacci_sequence = []
    a, b = 0, 1
    
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

# Generate and print the list of Fibonacci numbers up to 'n'
fib_sequence = generate_fibonacci_sequence(n)
print(f"Fibonacci sequence up to {n}: {fib_sequence}")

