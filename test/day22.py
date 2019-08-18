def btt(binary):
    decimal = i = 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def moin():
    mi = iter([1101101, 1101111, 1101001, 1101110])
    return "".join((chr(btt(next(mi))), chr(btt(next(mi))), chr(btt(next(mi))), chr(btt(next(mi)))))

if __name__ == "__main__":
    print(moin())
