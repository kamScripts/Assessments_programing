def read_file(input_file):
    """ Read text file and return list of words"""
    words_arr = []
    with open(input_file, 'r', encoding='UTF-8') as file:
        for line in file:
            line_list = line.rstrip('\n').split(' ')
            for word in line_list:
                words_arr.append(word.lower().rstrip(',').rstrip('.'))
    return words_arr

def count_words(input_file):
    """ Count words and return them in dictionary"""
    words_counted = {}
    words_arr = read_file(input_file)
    for word in words_arr:
        if word == '':
            continue
        if word not in words_counted:
            words_counted.update({f'{word}' : 1})
        else:
            words_counted.update({f'{word}' : words_counted.get(word)+1})
    return words_counted


def find_5_most_common(input_file):
    """ Find 5 most common words and return them in dictionary"""
    l = list(count_words(input_file).items())
    def get_second_element(item):
        return item[1]
    sorted_list = sorted(l, key=get_second_element, reverse=True)
    sorted_dict = {}
#    print(f'sorted list with {len(sorted_list)} elements: ', sorted_list)
    for i in range(5):
        sorted_dict.update({str(sorted_list[i][0]):sorted_list[i][1]})   
    return sorted_dict

print(find_5_most_common('test_text.txt'))
