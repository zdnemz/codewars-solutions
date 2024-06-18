# https://www.codewars.com/kata/5848565e273af816fb000449/python

def encrypt_this (text) :
    words = text.split()
    result = []

    for word in words:
        result.append(str(ord(word[0])) + word[1:][::-1])

    return " ".join(result)

print(encrypt_this("A wise old owl lived in an oak"))