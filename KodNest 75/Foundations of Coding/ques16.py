# Delete the Middle Node of a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle(head):
    # Write your code here
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head


def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(' '.join(vals))


def jprint(x):
    if isinstance(x, bool):
        print("true" if x else "false")
    elif isinstance(x, list):
        def conv(v):
            if isinstance(v, bool):
                return "true" if v else "false"
            if isinstance(v, list):
                return "[" + ", ".join(conv(i) for i in v) + "]"
            return str(v)

        print("[" + ", ".join(conv(i) for i in x) + "]")
    else:
        print(x)


import sys
data = sys.stdin.read().split()
it = iter(data)

def ni():
    return int(next(it))

def ns():
    return next(it)


n = ni()
head = ListNode(ni())
current = head

for i in range(1, n):
    current.next = ListNode(ni())
    current = current.next

result = delete_middle(head)
print_list(result)