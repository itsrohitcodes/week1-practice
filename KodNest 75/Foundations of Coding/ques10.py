# Asteroid Collision

def asteroid_collision(asteroids):
    # Write your code here ...
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
                break
            else:
                break

        else:
            stack.append(asteroid)

    return stack


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
asteroids = [ni() for _ in range(n)]

result = asteroid_collision(asteroids)
jprint(result)