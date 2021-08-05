# A function to find rank of a string in all permutations of characters
def findRank(st):
    ln = len(st)
    mul = fact(ln)
    rank = 1
    i = 0

    while i < ln:
        mul = mul / (ln - i)
        # count number of chars smaller than str[i] fron str[i + 1] to str[len-1]
        countRight = findSmallerInRight(st, i, ln - 1)
        rank = rank + countRight * mul
        i = i + 1
    return rank

st = input(": ")
print(findRank(st))