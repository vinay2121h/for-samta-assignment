def fibonacci_ss(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]


try:
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result =fibonacci_ss(n) #function calling on there
        print(f"Fibonacci sequence up to {n} terms: {result}")

except ValueError:
    print("Invalid input. Please enter a positive integer.")
