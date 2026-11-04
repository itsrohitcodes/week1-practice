# Maximum Twin Sum of a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Write your code here
def pairSum(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr:
        nxt = curr.next

        curr.next = prev
        prev = curr
        curr = nxt

    ans = 0
    first = head
    second = prev

    while second:
        ans = max(ans, first.val + second.val)
        first = first.next
        second = second.next

    return ans


n = int(input())
values = list(map(int, input().split()))

head = ListNode(values[0])
current = head

for i in range(1, n):
    current.next = ListNode(values[i])
    current = current.next

print(pairSum(head))