# The Fibonacci Sequence Task
def fibonacci_seq(n):
    if n < 0:
        print("Error. Enter a positive integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_seq(n - 1) + fibonacci_seq(n - 2)
print("Fibonacci Sequence: ")


for i in range(20):
    print(fibonacci_seq(i))
