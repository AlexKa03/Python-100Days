#Original Code:
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: # Changed from 4000 to 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2000))
print(is_leap(2020))
print(is_leap(1900))
print(is_leap(2021))
