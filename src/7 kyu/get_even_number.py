# https://www.codewars.com/kata/514a6336889283a3d2000001/train/python

def get_even_numbers (arr) :
    return [x for x in arr if x % 2 == 0]

print(get_even_numbers([2,4,5,6]))
print(get_even_numbers([1,2,3,4,5,6,7,8,9,10]))