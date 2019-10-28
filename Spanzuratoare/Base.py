import codecs
import random

words = codecs.open('cuvinte_de_verificat.csv','r','utf8')

def alphabet():
    alphabet = list(map(chr, range(65, 91)))
    alphabet.append(chr(536))
    alphabet.append(chr(538))
    alphabet.append(chr(194))
    alphabet.append(chr(258))
    alphabet.append(chr(206))
    alphabet.remove("Q")
    alphabet.remove("W") # aici am facut o mica schema, vazand ca nu apar literele respective in fisier
    alphabet.remove("Y") # am scos literele respective, daca ar fi sa am de fiecare data cuvinte random, as sterge liniile astea 3 cu ".remove"
    return "".join(alphabet)

def word_digest(word, alpha):
    word = word.replace("*", "")
    for char in word:
        if char is ';':
            return word.replace(";", ""), alpha
        else:
            word = word.replace(char, "")
            alpha = alpha.replace(char, "")

def auto_hangman(word):
    tries = 1
    temp = alpha
    while(tries < 10 and len(word) > 2):
        char = random.choice(temp) #aici se inlocuieste cu str(input()) pentru a face jocul sa fie manual
        if char in word:
            word = word.replace(char, "")
            temp = temp.replace(char,"")
        else:
            tries += 1
            temp = temp.replace(char, "")

    if tries == 10:
        return False
    return True

characters = alphabet()
Tries = 0
word_no = 1

for word in words:
    alpha = characters
    word = word.replace(str(word_no), "")[1:]
    word_no += 1
    word, alpha = word_digest(word, alpha)
    while(auto_hangman(word) == False):
        Tries += 1

print("Number of tries:",Tries)

# codul functioneaza dupa fisiere de tip *.csv cu format astfel: NR;CUVANT PARTIAL;CUVANT INTREG
# spre ex: 38;E*******LE;EXONDĂRILE