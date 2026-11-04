# Number of Recent Calls

from collections import deque


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


class RecentCounter:
    def __init__(self):
        self.calls = deque()

    def ping(self, t):
        self.calls.append(t)

        while self.calls[0] < t - 3000:
            self.calls.popleft()

        return len(self.calls)


import sys
data = sys.stdin.read().split()
it = iter(data)

def ni():
    return int(next(it))

def ns():
    return next(it)


n = ni()
recentCounter = RecentCounter()

for i in range(n):
    t = ni()
    jprint(recentCounter.ping(t))