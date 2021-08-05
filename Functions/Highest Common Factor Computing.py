def compute_hcf(x, y):
    if x > y:
        smaller = y
    elif y > x:
        smaller = x
    else:
        return x
    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

print(compute_hcf(num1, num2))
