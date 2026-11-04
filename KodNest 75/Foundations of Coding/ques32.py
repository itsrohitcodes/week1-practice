# Reverse Words in a Sentence

def reverse_words(s):
    # Write your code here ...
    words = s.split()
    reverse = words[::-1]
    reverse_sentence = ' '.join(reverse)

    return reverse_sentence


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


s = input()
jprint(reverse_words(s))