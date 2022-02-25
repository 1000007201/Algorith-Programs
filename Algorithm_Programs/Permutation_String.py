def to_string(_list):
    return "".join(_list)


def permute(string1, start_index,last_index):
    if start_index == last_index:
        print(to_string(string1))
    else:
        for i in range(start_index, last_index+1):
            string1[start_index], string1[i] = string1[i], string1[start_index]
            permute(string1, start_index+1, last_index)
            string1[start_index], string1[i] = string1[i], string1[start_index]


string = "ABC"
string_len = len(string)
string_list = list(string)
permute(string_list, 0, string_len-1)
