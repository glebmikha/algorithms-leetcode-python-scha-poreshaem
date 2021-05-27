def print_tree(arr, i=0, level=0):
    if i < len(arr):
        print_tree(arr, i=2 * i + 2, level=level + 1)
        print(3 * ' ' * level + str(arr[i]))
        print_tree(arr, i=2 * i + 1, level=level + 1)


def heapify(arr, i, n):
    l = 2 * i + 1
    r = 2 * i + 2

    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)


def heap_sort(arr):
    n = len(arr)
    # build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


if __name__ == '__main__':
    nums = [1, 8, 3, 0, 5]
    print_tree(nums)
    heap_sort(nums)
    print(nums)
