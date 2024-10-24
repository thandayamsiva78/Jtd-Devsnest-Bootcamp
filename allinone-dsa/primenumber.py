## Prime Number

"""A prime number is a number that can only be divided by 1 and itself without leaving remainder"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(8))
        