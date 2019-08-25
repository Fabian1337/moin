#heute schauen wir uns an wie man bin in decimal umawndelt ( eigene funktion ) und wir benutzen iter :D
def btd(binary):
    decimal = i = 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def moin():
    mi = iter([1101101, 1101111, 1101001, 1101110])
    return "".join((chr(btd(next(mi))), chr(btd(next(mi))), chr(btd(next(mi))), chr(btd(next(mi)))))

if __name__ == "__main__":
    print(moin())
