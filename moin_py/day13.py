def moin():
    marr = ["m", "o", "i", "n"]
    return "".join(list(k for k in marr)).format(**dict((k,k) for k in marr))

if __name__ == "__main__":
    print(moin())