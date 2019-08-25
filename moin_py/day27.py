class MinoniM:
    def center(self, s, l, h):
        while l > -1 and h < len(s) and s[l] == s[h]:
            l -= 1
            h += 1
        if self.maxLen < h-l-1:
            self.maxLen = h-l-1
            self.start = l+1

    def find(self, s):
        if s is "": return s
        self.maxLen = 0
        self.start = 0
        for i in range(len(s)):
            self.center(s, i, i), self.center(s, i, i+1)
        return s[self.start:self.start+self.maxLen]

def swap(s, x, y):
    arr = list(s)
    a, b = arr[x], arr[y]
    arr[x], arr[y] = b, a
    return "".join(arr)

def moin():
    mino = str(MinoniM().find("weqwrqqwrwrqsdfds894vbnsfadgd54vgesiftsadgdgsadgsseadggadsabcdefgfabinminonimfabianabcdefgksoasfadsf54asfavebieiatnafsfawrwrqwrqveadsfafs6c"))[:4]
    return swap(swap(mino, 2, 3), 1, 2)

if __name__ == "__main__":
    print(moin())