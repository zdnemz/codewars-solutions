# https://www.codewars.com/kata/545afd0761aa4c3055001386/train/python

def take(arr,n):
    return [] if n == 0 else arr[:n]

print(take([0, 1, 2, 3, 5, 8, 13], 3))