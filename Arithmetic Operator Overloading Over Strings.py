str_in = input("Input: ")

for i in str_in:
    if i == "+":
        index_of_plus = str_in.index(i)
        x = str_in[index_of_plus - 1]
        y = str_in[index_of_plus + 1]
        output = int(x) + int(y)
        if y == int(str_in[-1]):
            print(output)
        else:
            y = output

    elif i == "*":
        index_of_star = str_in.index(i)
        x = str_in[index_of_star - 1]
        y = str_in[index_of_star + 1]
        output = int(x) + (2 * int(y))
        if y == int(str_in[-1]):
            print(output)
        else:
            y = output
