def toT(hpair):
    return bytearray.fromhex(hpair).decode()

sixsixsix = [6,6,6] # number of the beast
dfe = ["d", "f", "e"]
sixtynine = "69" # sixty nine ^^ 
zipzip = [str(x[0]) + x[1] for x in zip(sixsixsix, dfe)]


def moin():
    return "".join((toT((zipzip[0])), toT((zipzip[1])), toT(sixtynine), toT((zipzip[2]))))

if __name__ == "__main__":
    print(moin())
