def prime_numbers_between(lower_num, upper_num):
    result = []
    for num in range(lower_num, upper_num + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                result.append(num)
    return result


x = int(input("Starting number: "))
y = int(input("Ending number: "))
print(prime_numbers_between(x, y))
