def list_insert(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result