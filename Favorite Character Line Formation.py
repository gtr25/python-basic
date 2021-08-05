# This code gets a Maximum Characters per line, Favorite Character and words separated by commas
# From all the possible combinations of the words,
# After excluding the "Favorite Character" and white space,
# if the total number of characters is less than the "Maximum Characters" given by the user,
# That specific combination of words is printed along with the number of characters other than fav char and whitespace


import itertools


def all_combinations(input_list):
    combinations = []
    for r in range(len(input_list) + 1):
        combinations += list(itertools.combinations(input_list, r))

    def join_tuple_string(strings_tuple) -> str:
        return ' '.join(strings_tuple)

    return list(map(join_tuple_string, combinations))


max_char = int(input("Max char per line: "))
fav_char = (input("Favorite character: ")).lower()
words = input("Words: ")
word_list = words.split(",")
result_list = []

for word in word_list:
    result_list.append(("".join([x for x in word if x.isalnum() is True])).lower())

combinations_list = all_combinations(result_list)

for combo in combinations_list:
    if len(combo) != 0:
        combo_count = 0
        for char in combo:
            if (char != ' ') and (char != fav_char):
                combo_count += 1

        if combo_count <= max_char:
            print("{} ({})".format(combo, combo_count))
