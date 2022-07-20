from curses import keyname
from PyMultiDictionary import MultiDictionary


alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
            12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: "y", 26: 'z'}

Uppercase = [x.upper() for x in alphabet.values()]
Lowercase = [x.lower() for x in alphabet.values()]


def encrypt(sentence, key):
    encrypted = ""
    for letter in sentence:
        if letter in Uppercase or letter in Lowercase:
            temp = list(alphabet.keys())[
                list(alphabet.values()).index(letter.lower())] + key
            if temp > 26:
                temp = temp % 26
        else:
            temp = letter
        if letter in Uppercase:
            encrypted += alphabet[abs(temp)].upper()
        elif letter in Lowercase:
            encrypted += alphabet[abs(temp)].lower()
        else:
            encrypted += temp
    return encrypted


def decrypt(sentence, key):
    return encrypt(sentence, -key)


def crack(str, shift):
    pass


if __name__ == "__main__":
    print(encrypt("apple", 20))
    print(decrypt("lmn", 10))
