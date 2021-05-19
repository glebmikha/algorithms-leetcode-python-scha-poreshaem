def bubble_sort(arr):
    # O(n**2)
    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr):
    # O(n**2)
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    # O(n**2)
    for i in range(1, len(arr)):
        j = i - 1
        cur_el = arr[i]
        while j >= 0 and cur_el < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = cur_el  # insert


def quick_sort_op(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[-1]

    less = [el for el in arr[:-1] if el < pivot]
    greater = [el for el in arr[:-1] if el >= pivot]

    return quick_sort_op(less) + [pivot] + quick_sort_op(greater)


def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]
    for j in range(start, end):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)


if __name__ == '__main__':
    nums = [4, 8, 2, 1, 3]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
