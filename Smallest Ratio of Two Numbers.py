num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


def compute_hcf(x, y):
    if x > y:
        smaller = y
    elif y > x:
        smaller = x
    else:
        return x
    hcf = None
    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


hcf_of_nums = compute_hcf(num1, num2)

val1 = int(num1 / hcf_of_nums)
val2 = int(num2 / hcf_of_nums)

if num1 != val1:
    print("{} : {} = {} : {}".format(num1, num2, val1, val2))
else:
    print("{} : {} can't be reduced any further".format(num1, num2))

