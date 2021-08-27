x = 10
print("x", x, id(x))
l = [1, 2, 3]
print("l", l, id(l))


def foo(w, k):
    print("w", w, id(w))
    print("k", k, id(k))
    w += 1
    k[0] = 111


foo(x, l)
print(x, l)
