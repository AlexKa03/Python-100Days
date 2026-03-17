def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(4))
print(is_leap(100))
print(is_leap(400))
print(is_leap(800))
print(is_leap(200))
print(is_leap(2000))
print(is_leap(2020))
print(is_leap(2021))
print(is_leap(1900))
