# A utility function to count smaller characters on right of arr[low]
def findSmallerInRight(st, low, high):
    countRight = 0
    i = low + 1
    while i <= high:
        if st[i] < st[low]:
            countRight = countRight + 1
        i = i + 1
    return countRight