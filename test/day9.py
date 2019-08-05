def moin():
    a = [(1 << 7)-19, int("10101110101010111010101111101111111111", base=2) & 111,int("0100001", base=2) | int("1001000", base=2), ~int("".join(['-', '1', '1', '1']), base=10)]
    return "".join([chr(c) for c in a])

if __name__ == "__main__":
    print(moin())
