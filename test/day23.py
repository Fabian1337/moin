def lstr(s): return str(chr(s))
def moin():
    val = int(bin(ord("👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋"[0])), 2) >> 10 &~ (1 << 4)
    return "".join(map(lstr, ((val | 0b1101111-6), val | 0b1101111, (val | 0b1101111-6) & 0b1101000 + 1, (val | 0b1101111**1) & 0b1101110)))

if __name__ == "__main__":
    print(moin())


