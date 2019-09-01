def swap(s, x, y):
    arr = list(s)
    a, b = arr[x], arr[y]
    arr[x], arr[y] = b, a
    return "".join(arr)

def moin():
    m = list(filter(None, "https://stackoverflow.com/questions/tagged/python".split("/")))
    del m[0]
    del m[2:]
    m[0] = m[0].split(".")[1]
    m[1] = swap(m[1][-4:-1], 0, 1)
    return m[0][-1] + m[1]

if __name__ == "__main__":
    print(moin())