# Dota2 Senate

def predict_party_victory(senate):
    # Write your code here ...
    radiant = []
    dire = []
    n = len(senate)

    for i in range(n):
        if senate[i] == 'R':
            radiant.append(i)
        else:
            dire.append(i)

    while len(radiant) > 0 and len(dire) > 0:
        r = radiant.pop(0)
        d = dire.pop(0)

        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)

    if len(radiant) > 0:
        return "Radiant"

    return "Dire"


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


senate = input()
jprint(predict_party_victory(senate))