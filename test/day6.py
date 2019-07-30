import string

def moin():
    return "".join([w[0] for w in ["morgens", "onaniere", "ich", "nicht"]])

if __name__ == "__main__":
    print(moin())