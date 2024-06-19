# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

def increment_string(s):
    import re
    match = re.search(r'(\d+)$', s)
    
    if match:
        number_str = match.group(1)
        prefix_str = s[:match.start()]
        
        incremented_number = str(int(number_str) + 1)

        incremented_number = incremented_number.zfill(len(number_str))

        return prefix_str + incremented_number
    else:
        return s + '1'

print(increment_string('foobar001'))
print(increment_string('foo'))
print(increment_string('foobar99'))
print(increment_string('foobar099'))
