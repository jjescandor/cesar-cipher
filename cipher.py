from curses import keyname
from distutils.dep_util import newer_pairwise
from PyMultiDictionary import MultiDictionary
from corpus_loader import word_list, name_list
import enum
import re


alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k',
            12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: "y", 26: 'z'}

Uppercase = [x.upper() for x in alphabet.values()]
Lowercase = [x.lower() for x in alphabet.values()]


def encrypt(sentence, key):
    encrypted = ""
    for letter in sentence:
        if letter in Uppercase + Lowercase:
            temp = list(alphabet.keys())[
                list(alphabet.values()).index(letter.lower())] + key
            if temp > 26:
                temp %= 26
            if temp <= -1:
                temp += 26
        if letter in Uppercase:
            encrypted += alphabet[abs(temp)].upper()
        elif letter in Lowercase:
            encrypted += alphabet[abs(temp)].lower()
        else:
            encrypted += letter
    return encrypted


def decrypt(sentence, key):
    return encrypt(sentence, -key)


def crack(encrypted_str):
    dictionary = MultiDictionary()
    words = encrypted_str.split(" ")
    optimize_list = []
    deciphered = ""
    key = []
    for word in words:
        for j in range(1, 26):
            new_word = ""
            search_word = ""
            for i, letter in enumerate(word):
                if letter in Uppercase + Lowercase:
                    temp = list(alphabet.keys())[
                        list(alphabet.values()).index(letter.lower())] + j
                    if temp > 26:
                        temp %= 26
                    new_word += alphabet[abs(temp)]
                    search_word += alphabet[abs(temp)]
                else:
                    new_word += letter
            if search_word in word_list + name_list:
                deciphered += f"{new_word} "
    if len(deciphered) > 0:
        for word in deciphered.split():
            if word in word_list + name_list and len(word) > 1:
                optimize_list.append(word)
    if len(optimize_list) > 0 and len(optimize_list)/len(words) > 0.5:
        for word in optimize_list:
            for j in range(1, 26):
                new_word = ""
                for i, letter in enumerate(word):
                    if letter in Uppercase + Lowercase:
                        temp = list(alphabet.keys())[
                            list(alphabet.values()).index(letter.lower())] + j
                        if temp > 26:
                            temp %= 26
                        new_word += alphabet[abs(temp)]
                    else:
                        new_word += letter
                if new_word in words:
                    length = list(alphabet.keys())[
                        list(alphabet.values()).index(new_word[0].lower())]
                    length1 = list(alphabet.keys())[
                        list(alphabet.values()).index(word[0].lower())]
                    if length - length1 < 0:
                        key.append((length + 26) - length1)
                    else:
                        key.append(length - length1)
        if len(key) and len(key)/len(optimize_list) > 0.8:
            return decrypt(encrypted_str, most_frequent(key))
    return ""


def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


if __name__ == "__main__":
    # dictionary = MultiDictionary()
    print(encrypt("I will always love you", 10))
    print(decrypt("S gsvv kvgkic vyfo iye", 10))
    print(crack("Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."))
