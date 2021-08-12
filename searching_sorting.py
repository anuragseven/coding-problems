# write code for merge sort

def merge(a, p, q, r):
   
    L = []
    R = []
    for i in range(p,q+1):
        L.append(a[i])
    for i in range(q+1,r+1):
        R.append(a[i])
    L.append((2 ** 31) - 1)
    R.append((2 ** 31) - 1)
    i = 0
    j = 0
    k = p

    while k <= r:
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1
        k = k + 1


def mergeSort(a, p, r):
    if p < r:
        q = int((p + r) / 2)
        mergeSort(a, p, q)
        mergeSort(a, q + 1, r)
        merge(a, p, q, r)


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quickSort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quickSort(a, p, q - 1)
        quickSort(a, q + 1, r)


def binarySearch(a, num):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l + r - 1) // 2
        if a[mid] == num:
            return mid
        if a[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    return -1


