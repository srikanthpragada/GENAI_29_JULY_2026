def isprime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isperfect(n):
    """Return True if n is a perfect number, else False."""
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

