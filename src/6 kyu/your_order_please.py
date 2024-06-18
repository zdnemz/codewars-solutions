# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    if sentence == "":
        return ""
    
    words = sentence.split()
    
    def get_number(word):
        for char in word:
            if char.isdigit():
                return int(char)
        return 0
    
    sorted_words = sorted(words, key=get_number)
    
    return " ".join(sorted_words)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
