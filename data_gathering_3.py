from modules import frequency_dict, alphabet_dict, caesering, matrica, math, dic_quicksort, text_cleaner, count_letter, send_me_a_mess, requests
from random import randint
from datetime import datetime
from json import load, dump
from os import listdir
from sys import setrecursionlimit, exit

language_array = ['en', 'ua']
language = str(input("Only 'en' or 'ua' available>>>"))
if language not in language_array:
    print('You wrote wrong language')
    exit()

print("Started working")
situation = {}
file_array = listdir('templates/'+language)   #it should or may be changed

start = datetime.now()
q_time = start
alphabet_count = count_letter[language]
setrecursionlimit(10000)
alphabet = alphabet_dict[language]

average_dict = {}

pos_of_book = 0
try:
    for document_name in file_array:
        start_point = 0

        #reading document

        with open('templates/'+language+'/'+document_name, 'r', encoding='utf8') as r:
            context = r.read()

        #analysing

        count = 0
        sum = 0

        while True:
            #getting random key (it doesn't even matter)
            key = randint(0, 25)
            new_alphabet = caesering(key,language)

            end_point = context.find('.', start_point+1)

            if end_point == -1:
                pos_of_book += 1
                print(str(pos_of_book) + ') ' + str(start_point))
                print(datetime.now() - q_time)
                print('\n')
                q_time = datetime.now()
                break

            #getting text
            text = context[start_point:end_point]
            length = end_point - start_point
            text, q = text_cleaner(text, language)
            length -= q

            if length == 0:
                start_point = end_point + 1
                continue

            # enciphering
            for length_now in range(1, length+1):
                text_list = list(text[:length_now])
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

                # enciphering is finished
                enciphered_text = result

                # checking if key is in linquist method
                array = matrica(math(enciphered_text, language))

                statement = int(key) in array
                length_of_array = len(array)
                
                #test

                if length_of_array == alphabet_count:
                    step_of_success = 4
                elif length_of_array == 1:
                    step_of_success = 0
                elif length_of_array < 4:
                    step_of_success = 1
                elif length_of_array <= alphabet_count//2:
                    step_of_success = 2
                else:
                    step_of_success = 3
                
                #Failed ciphering
                try:
                    situation[length_now][statement] += 1
                    if statement:
                        for i in range(step_of_success, 5):
                            situation[length_now]['param'][i] += 1
                    
                    average_dict[length_now]['length'] += length_of_array
                    average_dict[length_now]['times'] += 1
                except KeyError:
                    situation[length_now] = {True: 0, False: 0, 'param': [0, 0, 0, 0, 0]}
                    situation[length_now][statement] += 1
                    if statement:
                        for i in range(step_of_success, 5):
                            situation[length_now]['param'][i] += 1
                    
                    average_dict[length_now] = {'length': length_of_array, 'times': 1}

            start_point = end_point
            count += 1
            

except KeyboardInterrupt:
    keys = []
    values = []
    for key, value in situation.items():
        keys.append(key)
        values.append(value)
    print(len(keys))
    keys, values = dic_quicksort(keys, values)
    for numb in range(0, len(keys)):
        situation[keys[numb]] = values[numb]
    
    print('broken')

print('///')
print(datetime.now()-start)
#writing results
result = '\\\\ Input data ///\n'
result += 'Length of ciphering text: ' + str(length) + '\n'
result += 'Input file name: ' + document_name + '\n'
result += '/// Results \\\\ \n'
for key, sit in situation.items():
    result += '\nLength is ' + str(key) + '.\n'
    result += 'Trues are ' + str(sit[True]) + ', and Falses are ' + str(sit[False]) + '.\n'
result += 'Sum is ' + str(count) + '.'
result += '\nAnalysing time is ' + str(datetime.now()-start) + '.'

with open('results_2.txt', 'w') as w:
    w.write(result)

#writing results for analysing.py
with open('results_2_' + language + '.json', 'w') as w:
    dump(situation, w)

keys = []
values = []
for key, value in average_dict.items():
    keys.append(key)
    values.append(value)
print(len(keys))
keys, values = dic_quicksort(keys, values)
for numb in range(0, len(keys)):
    average_dict[keys[numb]] = values[numb]

with open('average_keys_per_length.json', 'w') as w:
    dump(average_dict, w)
