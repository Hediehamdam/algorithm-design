def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    temp = []

    # merge two halves
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # remaining left side
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # remaining right side
    while j <= high:
        temp.append(arr[j])
        j += 1

    # copy back
    for k in range(len(temp)):
        arr[low + k] = temp[k]


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

    return arr
