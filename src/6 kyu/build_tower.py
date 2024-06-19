# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    result = []
    for i in range(n_floors):
        space = " " * (n_floors - i - 1)
        floor = "*" * ((i * 2) + 1)

        result.append(space + floor + space)
    return result

print(tower_builder(5))
print(tower_builder(3))