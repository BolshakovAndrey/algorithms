dataset = [int(a) for a in input().split(' ')]
k = int(input())


def calculate(data_set, k: int):
    """
    :param data_set: input dataset
    :param k: - number of University
    :return: sorted University IDs
    """
    id_list = {}
    for i in data_set:
        if i not in id_list:
            id_list[i] = 1
        else:
            count = id_list.get(i)
            count += 1
            id_list[i] = count

    result = sorted(id_list, key=(lambda key: id_list[key]), reverse=True)
    print(*result[:k])


calculate(dataset, k)
