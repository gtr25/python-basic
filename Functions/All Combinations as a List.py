import itertools


def all_combinations(input_list):
    combinations = []
    for r in range(len(input_list) + 1):
        combinations += list(itertools.combinations(input_list, r))

    def join_tuple_string(strings_tuple) -> str:
        return ' '.join(strings_tuple)

    return list(map(join_tuple_string, combinations))


x_list = ['A', 'B', 'C']
print(all_combinations(x_list))
