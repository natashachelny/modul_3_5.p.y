def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number[0])
result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(123)

print(result1)
print(result2)