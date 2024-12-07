def manual_find(lst, target):
    i = 0
    for e in lst:
        if e == target:
            return i
        i += 1
    return -1
