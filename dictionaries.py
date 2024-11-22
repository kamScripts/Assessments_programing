def read_file(input_file):
    words_arr = []
    with open(input_file, 'r', encoding='UTF-8') as file:
        for line in file:
            line_list = line.rstrip('\n').split(' ')
            for word in line_list:
                    words_arr.append(word.lower())
    return words_arr
    
    

def count_words(input_file):
    words_counted = {}
    words_arr = read_file(input_file)
    for word in words_arr:
        if word not in words_counted.keys():
            words_counted.update({f'{word}' : 1})
        else:
           words_counted.update({f'{word}' : words_counted.get(word)+1})
    return words_counted
print(count_words('test_text.txt'))

def find_5_most_common(d):
    l =list(d)
    print(l)
            
        

    