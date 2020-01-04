from modules import math, matrica, caesering, frequency_dict, alphabet_dict, count_letter

language = str(input("enter language>>>"))
enciphered_text = str(input("text>>>"))
length_of_alphabet = count_letter[language]

array = matrica(math(enciphered_text, language))
print(array)
list_text = list(enciphered_text)
alphabet = alphabet_dict[language]
for i in array:
    new_alphabet = caesering(length_of_alphabet-i, language)
    result = ''
    for i in list_text:
        try:
            if i == i.upper():
                ind = alphabet.index(i.lower())
                result += new_alphabet[ind].upper()
            else:
                ind = alphabet.index(i)
                result += new_alphabet[ind]
        except:
            result += i
    print(result)
