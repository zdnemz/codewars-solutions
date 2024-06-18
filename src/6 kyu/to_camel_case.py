# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    words = text.replace("-", "_").split("_")
    
    if words[0].istitle():
        camel_case_text = words[0] + ''.join(word.title() for word in words[1:])
    else:
        camel_case_text = words[0].lower() + ''.join(word.title() for word in words[1:])
    
    return camel_case_text

print(to_camel_case("the-stealth-warrior")) 
print(to_camel_case("The_Stealth_Warrior")) 
print(to_camel_case("The_Stealth-Warrior")) 
