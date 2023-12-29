import math

def is_prime(n):
    if n <= 1:
        return "Not prime"
    if n == 2:
        return "Prime"
    if n % 2 == 0:
        return "Not prime"
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return "Not prime"
    return "Prime"

T = int(input())
for _ in range(T):
    n = int(input())
    result = is_prime(n)
    print(result)