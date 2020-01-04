import requests
frequency_dict = {'en': ['e', 't', 'a', 'o', 'n', 'i', 'r', 's', 'h'], 'ua': ['о', 'а', 'н', 'і', 'и', 'в', 'р', 'т', 'е', 'с', 'к', 'л']}
alphabet_dict = {
    'en': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'ua': ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'й', 'і', 'ї', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
}
count_letter = {'en': 26, 'ua': 33}

def dict_maker(lang, just_numbers=False):
    global alphabet_dict 
    arr = alphabet_dict[lang]
    dict0 = {}

    if just_numbers:
        for i in range(0, len(arr)):
            dict0[i] = 0
    else:
        for i in arr:
            dict0[i] = 0
    
    return dict0

def math(text, lang):
    dic = dict_maker(lang)

    for i in text:
        if i.lower() in dic.keys():
            dic[i.lower()] = dic[i.lower()] + 1

    res = []

    values = list(dic.values())
    keys = list(dic.keys())
    compare_number = max(values) - 1

    while True:
        position_exception = 0
        for i in range(0, len(values)):
            i -= position_exception
            if values[i] > compare_number:
                res.append(keys[i])
                del values[i]
                del keys[i]
                position_exception += 1
        
        if len(res) < 4:
            compare_number = max(values) - 1
        else:
            break
    return res, lang

def matrica(lis):
    global alphabet_dict
    global frequency_dict
    global count_letter

    array, lang = lis[0], lis[1]
    matric = []
    dic =  dict_maker(lang, just_numbers=True)
    alphabet = alphabet_dict[lang]
    frequency_array = frequency_dict[lang]

    for _ in range(0, len(frequency_array)):
        matric.append([])

    for freq in frequency_array:
        for i in array:
            q = alphabet.index(i) - alphabet.index(freq)
            if q < 0:
                q += count_letter[lang]
            matric[frequency_array.index(freq)].append(q)
            dic[q] = dic[q] + 1
    predpolozhenie = []

    max_numb = max(dic.values())-1
    
    for key, value in dic.items():
        if value > max_numb:
            predpolozhenie.append(key)
    
    return predpolozhenie

def caesering(key, lang):
    global alphabet_dict
    alphabet = alphabet_dict[lang]

    if key in alphabet:
        key = alphabet.index(key)
    else:
        key = int(key)
    
    new_alphabet = alphabet[key:] + alphabet[:key]
    return new_alphabet

def dic_quicksort(keys, values):
    keys_lower = []
    keys_upper = []
    values_lower = []
    values_upper = []

    if keys == []:
        return [], []

    opora = keys[0]

    for numb in range(1, len(keys)):
        if keys[numb] < opora:
            keys_lower.append(keys[numb])
            values_lower.append(values[numb])
        elif keys[numb] > opora:
            keys_upper.append(keys[numb])
            values_upper.append(values[numb])
    
    keys_lower, values_lower = dic_quicksort(keys_lower, values_lower)
    keys_upper, values_upper = dic_quicksort(keys_upper, values_upper)

    return_keys = keys_lower + [opora] + keys_upper
    return_values = values_lower + [values[0]] + values_upper

    return return_keys, return_values

def text_cleaner(text, lang):
    global alphabet_dict
    alphabet = alphabet_dict[lang]
    count_of_deleted_symbols = 0
    finish_text = ""
    for i in list(text):
        if i.lower() not in alphabet:
            count_of_deleted_symbols += 1
        else:
            finish_text += i

    return finish_text, count_of_deleted_symbols

def send_me_a_mess(text):
    url = 'https://api.telegram.org/1067397016:AAF5eENyPqL7U5iu-X9HsNxQcxNESIAFyyU/'
    chat = 356397319
    params = {'chat_id': chat, 'text': text, 'parse_mode': 'Markdown'}
    response = requests.post(url + 'sendMessage', data=params)
    print(response.text())
    return response