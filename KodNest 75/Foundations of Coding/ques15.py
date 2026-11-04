# Odd-Even Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head):
    # Write your code here ...
    if head is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

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

if n == 0:
    print()
    raise SystemExit

head = ListNode(ni())
current = head

for i in range(1, n):
    current.next = ListNode(ni())
    current = current.next

result = odd_even_list(head)
print_list(result)