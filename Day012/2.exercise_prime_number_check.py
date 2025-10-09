def is_prime(num):
    if num <= 1 and num ==1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

print(is_prime(75))
print(is_prime(73))
print(is_prime(107))
print(is_prime(115))
print(is_prime(20))
print(is_prime(1))  # Edge case: 1 is not a prime number
