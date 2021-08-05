import more_itertools as mi

alphadict = {i: chr(i + 96) for i in range(1, 27)}

nums = input(": ")

partitions_of_input = list(mi.partitions(nums))

res = list()
for partition in partitions_of_input:
    temp = list()
    for li in partition:
        temp.append(''.join(li))
    res.append(temp)

for x in range(len(res)):
    for y in range(len(res[x])):
        res[x][y] = int(res[x][y])

output = []
for mn in res:
    st = ""
    for i in mn:
        if int(i) > 26 or i == 0:
            st = ""
            break
        else:
            st += alphadict.get(i)
    if st:
        output.append(st)

print("The {} possible decoded results are: ".format(len(output)))
for decoded in output:
    print(decoded)
