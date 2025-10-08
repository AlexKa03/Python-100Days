def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

is_leap_year(2000)
is_leap_year(2020)
is_leap_year(2024)
is_leap_year(2400)
is_leap_year(1700)
is_leap_year(1989)
is_leap_year(2100)
year = int(input("Enter a year: "))