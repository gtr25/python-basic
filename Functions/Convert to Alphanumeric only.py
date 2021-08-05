import string


def alpha_numeric():
    alphabet_list = list(string.ascii_lowercase)
    alphabet_list += list(string.ascii_uppercase)
    for i in range(10):
        alphabet_list.append(i)
    return alphabet_list


def convert_to_alphanumeric_only(input_list):
    alpha_numeric_only_list = alpha_numeric()
    output_string = ''
    for input_list_element in input_list:
        if input_list_element in alpha_numeric_only_list:
            output_string += input_list_element

    return output_string


print(convert_to_alphanumeric_only("h#eL%l&o,  !W@orld").lower())
