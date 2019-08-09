def moin():
    return "".join(list(map(lambda m: chr(int(m * 2)) , [54.5, 55.5, 52.5, 55.0])))

if __name__ == "__main__":
    print(moin())