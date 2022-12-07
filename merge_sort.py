from random import seed, shuffle

seed(1)
testlist = [i for i in range(10)]

shuffle(testlist)
print(testlist)


def merge(left, right):
    i = j = k = 0

    # careful here cuz call by ref langs might cause destructive sorting
    result = left + right

    # my version of the merge
    while len(left[i:]) > 0 or len(right[j:]) > 0:
        # if left is empty
        if len(left[i:]) <= 0:
            result[k] = right[j]
            j += 1
        # if right is empty
        elif len(right[j:]) <= 0:
            result[k] = left[i]
            i += 1
        elif left[i] <= right[j]:
            result[k] = left[i]
            i += 1
        elif right[j] < left[i]:
            result[k] = right[j]
            j += 1
        k += 1

    return result


def mergeSort(list):
    mid = len(list) // 2

    if len(list) == 1:
        return list
    else:
        return merge(mergeSort(list[:mid]), mergeSort(list[mid:]))


print(mergeSort(testlist))

