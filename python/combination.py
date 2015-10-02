import unittest


def unique(data):
    unique = []
    for n in data:
        if n not in unique:
            unique.append(n)
    return unique


def find_combination(num_list, target_sum):
    output = []
    num_list = sorted(num_list)
    # augment the list, anything that is > target_sum are discarded
    num_list = [n for n in num_list if n <= target_sum]

    #num_list = unique(num_list)
    print(num_list)

    if target_sum in num_list:
        # include the target_sum in the output
        output.append([target_sum])

    num_len = len(num_list)

    for i in range(num_len):
        for j in range(num_len):
            if i != j and (target_sum - num_list[i]) == num_list[j]:
                output.append(sorted([num_list[i], num_list[j]]))


    return unique(output)

if __name__ == '__main__':
    output = find_combination(
        num_list=[5, 5, 5, 15, 10, 20, 67, 100, 56], target_sum=15)
    output1 = find_combination(num_list=[5,5,5,10,15], target_sum=10)
    output2 = find_combination(num_list=[5,5,5,10], target_sum=5)
    print(output)
    print(output1)
    print(output2)
