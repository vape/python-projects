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


def merge_sort(l):
    return l if len(l) <= 1 else _merge_lists(merge_sort(l[0:len(l) // 2]),
                                              merge_sort(l[len(l) // 2:]))


def bubble_sort(l):
    for i in range(0, len(l)):
        i1, i2, swap = 0, 1, False
        while i2 < len(l) - i:
            if l[i1] > l[i2]:
                swap = True
                l[i1], l[i2] = l[i2], l[i1]
            i1 += 1
            i2 += 1
        if not swap:
            break


if __name__ == '__main__':
    #rl = list(range(-10, 50))
    #shuffle(rl)
    #print(rl)
    #print(merge_sort(rl))

    rl = list(range(-10, 100))
    shuffle(rl)
    bubble_sort(rl)
    print(rl)
