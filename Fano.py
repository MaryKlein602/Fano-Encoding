import json

# Reading the file
doc = open('Індивідуальні завдання з теми _Алгоритми кодування.txt', 'r', encoding='utf-8')
f = open('Encoded.txt','w', encoding='utf-8')

task = doc.read()
f.write('The Original Text\n\n\n')
for letter in task:
    f.write('{}'.format(letter))

# Creating a dictionary for unique symbols in text
good_code = []

def dict_making(file):

    # creating a dictionary for saving data about symbols and coding
    dict = {}
    for letter in list(set(file)):
        dict[letter] = [round((file.count(letter)) / (len(file)), 3), '']

    # for useful iterationgs creating a list with sorted elements of dictionary
    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
    return dict, sorted_dict

def split_in_two(dictionary, list):

    rs_list = []
    ls_list = []
    left_sum = 0
    right_sum = 0

    if len(list) > 1:

        for j in range(len(list)):

            if left_sum < sum(i[1][0] for i in list) / 2:
                left_sum += list[j][1][0]
                ls_list.append(list[j])
            else:
                right_sum += list[j][1][0]
                rs_list.append(list[j])

        if len(rs_list) == 0:
            rs_list.append(ls_list[-1])
            ls_list.remove(ls_list[-1])

    for i in ls_list:
        dictionary[i[0]][1] += '0'

        if len(ls_list) == 1:
            good_code.append(i[1][1])

    for i in rs_list:
        dictionary[i[0]][1] += '1'

        if len(rs_list) == 1:
            good_code.append((i[1][1]))

    sort_dict = sorted(dictionary.items(), key=lambda kv: kv[1])
    return dictionary, sort_dict

def binary_tree(dict, sort_dict):
    encoding_values = list(set(i[1][1] for i in sort_dict))
    for i in encoding_values:
        if i in good_code:
            continue

        new_list = []
        for j in range(len(sort_dict)):

            if sort_dict[j][1][1] == i:
                new_list.append(sort_dict[j])

        dict, sort_dict = split_in_two(dict, new_list)

    sort_dict = sorted(dict.items(), key=lambda kv: kv[1][0])
    return dict, sort_dict

def algorithm():

    dict, sort_dict = dict_making(task)
    dict, sort_dict = split_in_two(dict, sort_dict)

    while len(good_code) < len(dict):
        dict, sort_dict = binary_tree(dict, sort_dict)

    for i in dict:
        print('"{}"'.format(i), dict[i])
    return dict

dictionary = algorithm()

f.write('\n\nThe Shanon-Fano Encoding:\n\n')
for letter in task:
    f.write('{}'.format(dictionary[letter][1]))