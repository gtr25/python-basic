from itertools import permutations
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


# Gets two user input strings and converts it into a lowercase, alphanumerics only string.
# It is assigned to S1 and S2 respectively
S1 = (convert_to_alphanumeric_only(input("String 1: "))).lower()
S2 = (convert_to_alphanumeric_only(input("String 2: "))).lower()

permutations_of_list1 = list(permutations(S1))
tupled2 = tuple(S2)

if tupled2 in permutations_of_list1:
    print("Yes")
else:
    print("No")
