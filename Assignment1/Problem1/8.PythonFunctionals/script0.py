# Map and Lambda Function

def cube(x): return x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers

    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
