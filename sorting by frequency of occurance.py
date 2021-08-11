arr_size = int(input("Enter Array Size: "))
arr_in = input("Enter Array: ")

input_list = arr_in.split(",")
for i in range(0, len(input_list)):
    input_list[i] = int(input_list[i])

new_list = sorted(list(set(input_list)))  # This creates a list with no repeating elements
for j in range(0, len(new_list)):
    new_list[j] = int(new_list[j])

count_list = []
for new_num in new_list:
    count_list.append(int(input_list.count(new_num)))

count_dict = {}
for key in new_list:
    for value in count_list:
        count_dict[key] = value
        count_list.remove(value)
        break

res_dict = {k: v for k, v in sorted(count_dict.items(), key=lambda item: item[1])}

out_list = []
for m in list(res_dict.keys()):
    temp = ",".join([str(m) for _ in range(int(res_dict[m]))])
    out_list.append(temp)

print(",".join(out_list))
