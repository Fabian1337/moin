m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

m[12] = 1
m[40] = 1
m[8] = 1
m[39] = 1

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def swap(s, x, y):
    arr = list(s)
    a, b = arr[x], arr[y]
    arr[x], arr[y] = b, a
    return "".join(arr)

def imno():
    for i, v in enumerate(m):
        if v == 1:
            yield list(letters[i])

def moin():
    imnon = "".join([x[0] for x in list(imno())])
    imnon = swap(imnon, 0, 1)
    imnon = swap(imnon, 1, 3)
    imnon = swap(imnon, 2, 3)
    return "".join(imnon).lower()

if __name__ == "__main__":
    print(moin())
