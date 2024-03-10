'''
author = monini-ka (discord: raw.anomaly)
'''

import string

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

MEMBERS = { 'bob': '123',
            'ann': 'pass123',
            'mike': 'password123',
            'liz': 'pass123'
            }
# 1. Greet or welcome the user to the app

print('Welcome to the application. Please log in: ')

# 2. Ask the user for entering username and password
# 3. Check whether the password and username entered are among those registered 
#(including pairing).

while True:
    jmeno = (input('USERNAME: '))
    if jmeno in MEMBERS: ## MEMBERS.keys() neni nutne, protoze 'in' hleda v klicich sam od sebe
        #pass
        #print()
        break
    print('Wrong username, please try again.')
#print()

while True:
    heslo = (input('PASSWORD: '))
    if heslo in MEMBERS[jmeno]:
        #print()
        break
    print('Wrong password, please try again.')

print('Thank you.')

# 4. Ask the user to select among the three texts stored in the variable TEXTS.
print ('We have 3 texts to be analyzed.')

while True:
    vyber_textu = int(input('Enter a number btw. 1 and 3 to select: '))
    if 0 < vyber_textu <= len(TEXTS):
        vybrany_text = TEXTS[vyber_textu -1]
        break
    print('The chosen number must be 1, 2 or 3.')
#print(type(vybrany_text))  
print('Thank you.')

# 5. Calculate the following statistics for the selected text:#
#    a) number of words in total
slova = vybrany_text.split()
print('There are', len(slova), 'words in the selected text.')

#    b) number of words starting with capital letter
cap_slova = 0
for slovo in slova:
    if slovo[0].isupper():
        cap_slova += 1

print('There are', cap_slova, 'titlecase words.')

#    c) number of uppercase words
upp_slova = 0   #muzu nechat pojmenovani cap_slova protoze dynamicky jazyk
for slovo in slova:
    if slovo.isupper():
        upp_slova += 1

print('There are', upp_slova, 'uppercase words.')

#    d) number of lowercase words
low_slova = 0 
for slovo in slova:
    if slovo[0].islower():
        low_slova += 1

print('There are', low_slova, 'lowercase words.')

#    e) number of numeric-only words (e.g. 100, not 100N)
num_slova = []
for slovo in slova:
    if slovo.isnumeric():
        num_slova.append(slovo)

print('There are', len(num_slova), 'numeric strings')

#6. Create a bar chart depicting the frequencies of word lengths in the text. 
table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
delky = {}

for slovo in slova:
    slovo = slovo.translate(table).replace(' ', '') 
    l = len(slovo)

    #buď 
#   if l not in delky:
#        delky[l]=0
#    delky[l] += 1

    # anebo 
    delky[l] = delky.get(l,0) + 1

for delka in sorted(delky.keys()):
    vyskyt = delky[delka]
    print(delka, '*̈́' * vyskyt, vyskyt)

#7. Calculate the sum of all the numeric "words" in the given text.
sou_slova = 0

for slovo in num_slova:
    sou_slova += float(slovo)

print('If we summed all the numbers in this text we would get:', sou_slova)