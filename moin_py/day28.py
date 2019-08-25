vals = {".": 1, "-": 2, ")": 5, "(": 10, "#": 20, "+":50}

def calc(s):
    return chr(sum([vals[x] for x in list(s)]))

def moin():
    return "".join(map(calc, ["++)--", "#####(.", "((((((((((.....", "())##..)...##"]))

if __name__ == "__main__":
    print(moin())