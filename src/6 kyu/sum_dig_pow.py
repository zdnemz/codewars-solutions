# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

def sum_dig_pow(a, b):
    result = []
    for num in range(a, b + 1):
        digits = list(map(int, str(num)))
        if num == sum(d ** (i + 1) for i, d in enumerate(digits)):
            result.append(num)
    return result

print(sum_dig_pow(1, 10))
print(sum_dig_pow(10,89))
print(sum_dig_pow(1, 100))
print(sum_dig_pow(90, 100))