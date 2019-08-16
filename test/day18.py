def moin():
    mmmm = ["moin"]*4
    return "".join([list(mmmm[i])[i] for (i,s) in enumerate(mmmm)])

if __name__ == "__main__":
    print(moin())
