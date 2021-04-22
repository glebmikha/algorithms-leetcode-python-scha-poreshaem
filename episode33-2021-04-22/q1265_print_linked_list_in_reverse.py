class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def printValue(self):
        print(self.data)

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, node):
        self.head = node

    def insert_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def __repr__(self):
        s = ''
        tmp = self.head
        while tmp:
            s = s + str(tmp.data) + '-->'
            tmp = tmp.next
        return s

    def get_arr(self):
        arr = []
        tmp = self.head
        while tmp:
            arr.append(tmp)
            tmp = tmp.next
        return arr


ll = LinkedList(Node(1))
ll.insert_at_beginning(Node(2))
ll.insert_at_beginning(Node(3))


def print_in_reverse(head):
    arr = []
    tmp = head
    while tmp:
        arr.append(tmp)
        tmp = tmp.getNext()

    for el in arr[::-1]:
        el.printValue()


def print_in_reverse_rec(head):
    next = head.getNext()

    if not next:
        head.printValue()
        return
    else:
        print_in_reverse_rec(next)

    head.printValue()
    return


# print_in_reverse_rec(ll.head)

arr = [1, 2, 3]


def print_for_loop(arr):
    for i in range(len(arr)):
        print(arr[i])


def print_for_loop_rec(arr):
    if len(arr) < 1:
        return
    print(arr[0])
    print_for_loop_rec(arr[1:])


def get_max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


def get_max_rec(arr):
    if len(arr) <= 1:
        return arr

    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = get_max_rec(arr[1:])

    return arr[0] if arr[0] > sub_max else sub_max


# wimp solution
def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
    return m if m > list[0] else list[0]


arr = [1]
print(Max(arr))
