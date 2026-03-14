def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
        
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

is_prime(73)
is_prime(75)
is_prime(7)
is_prime(4)
is_prime(2)
is_prime(1)
