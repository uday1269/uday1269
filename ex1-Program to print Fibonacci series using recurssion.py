def fibonacci_tail_recursive(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tail_recursive(n-1, b, a+b)
terms = 10
for i in range(terms):
    print(fibonacci_tail_recursive(i))
