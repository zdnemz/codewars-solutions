# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines) :
    if(not lines) :
        return []
    result = []

    for i in range(len(lines)) :
        result.append(f'{i + 1}: {lines[i]}')

    return result

print(number([]))
print(number(['a', 'b', 'c']))
