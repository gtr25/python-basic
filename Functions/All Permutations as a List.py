import itertools


def permutation_list(str_in):
    y = list(itertools.permutations(str_in))

    def join_tuple_string(strings_tuple) -> str:
        return ' '.join(strings_tuple)

    return list(map(join_tuple_string, y))


x = ['A', 'B', 'C']
print(permutation_list(x))
