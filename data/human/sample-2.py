def fib_seq(limit):
    a, b = 0, 1
    result = []
    while len(result) < limit:
        result.append(a)
        a, b = b, a + b
    return result
