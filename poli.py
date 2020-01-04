from modules import caesering, alphabet

key = input('key>>>')
new_alphabet = caesering(key)
text = input('Text>>>')

text_list = list(text)
result = ''
for i in text_list:
    try:
        if i == i.upper():
            ind = alphabet.index(i.lower())
            result += new_alphabet[ind].upper()
        else:
            ind = alphabet.index(i)
            result += new_alphabet[ind]
    except:
        result += i

print('result is:')
print(result)

