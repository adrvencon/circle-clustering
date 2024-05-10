def transpose_list_of_lists(list_of_lists):
    transposed = [[] for _ in range(len(list_of_lists[0]))]
    
    for sublist in list_of_lists:
        for i, element in enumerate(sublist):
            transposed[i].append(element)
    
    return transposed