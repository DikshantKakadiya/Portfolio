import time
from Crypto.Util.number import getPrime

def factorize_naive(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

for n in range(10, 32):
    p = getPrime(n)
    q = getPrime(n)
    n = p * q
    start_time = time.time()
    factors = factorize_naive(n)
    duration = time.time() - start_time
    print(f"{n} = {p} x {q} = {factors[0]} x {factors[1]}  (duration: {duration:.4f}s)")
