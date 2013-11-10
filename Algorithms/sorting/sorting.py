from random import shuffle


def _merge_lists(l1, l2):
    nl = []
    while l1 or l2:
        if not l1:
            ll = l2
        elif not l2:
            ll = l1
        else:
            ll = l1 if l1[0] <= l2[0] else l2
        nl.append(ll.pop(0))

    return nl


def merge_sort_recursive(l):
    return l if len(l) <= 1 else _merge_lists(merge_sort_recursive(l[0:len(l) // 2]),
                                              merge_sort_recursive(l[len(l) // 2:]))


if __name__ == '__main__':
    rl = list(range(-10, 50))
    shuffle(rl)
    print(rl)
    print(merge_sort_recursive(rl))
