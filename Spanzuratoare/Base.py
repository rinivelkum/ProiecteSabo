import codecs
import random

words = codecs.open('cuvinte_de_verificat.csv','r','utf8')
random_number = random.randint(1,100) # daca se doreste identificarea unui cuvant anume, se inlocuieste aici cu int(input())

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

def select_word():
    i = 1
    for word in words:
        if i == random_number:
            return word.replace(str(random_number), "")[1:]
        i += 1

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
    alpha = characters
    while(tries < 10 and len(word) > 1):
        char = random.choice(alpha) #aici se inlocuieste cu str(input()) pentru a face jocul sa fie manual
        print(char) # pentru debugging, sa vad ce introduce pc-ul
        if char in word:
            word = word.replace(char, "")
            alpha = alpha.replace(char,"")
        else:
            tries += 1
            alpha = alpha.replace(char, "")

    if tries == 10:
        return False
    return True

characters = alphabet()
random_word = select_word()
random_word, characters = word_digest(random_word, characters)
Tries = 0
while(auto_hangman(random_word) == False):
    Tries += 1
    print("-------------------------------------") #debugging
print("Number of tries:",Tries)
print("Word to find out:",random_word)

# codul functioneaza dupa fisiere de tip *.csv cu format astfel: NR;CUVANT PARTIAL;CUVANT INTREG
# spre ex: 38;E*******LE;EXONDĂRILE