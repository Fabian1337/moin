
def find2un(arr):
    if len(arr) < 2:
        return len(arr)
    a, b = arr[0], arr[1]

    lastn = b
    lastn_count = (a == b)
    length = maxL = 1

    for n in arr[1:]:
        if n in (a, b):
            length += 1
            if b == n:
                lastn_count += 1
            else:
                lastn = a
                lastn_count = 1
        else:
            a = lastn
            b = n
            lastn = b
            length = lastn_count + 1
        maxL = max(length, maxL)
    return maxL


def moin():
    val_arr = []
    for val in [109, 111, 105, 110]:
        num = find2un([8, 9, 8, 5, 2, 5, 2, 7, 5, 4, 5, 4, 8, 5, 8, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5,
                       7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 5, 5, 5, 9, 8, 7, 4, 5, 2, 5, 4, 2, 7, 5, 5, 4, 8, 7, 5, 5, 8])
        while num != val:
            num += 1
        val_arr.append(num)
    return "".join(map(chr, val_arr))

if __name__ == "__main__":
    print(moin())
