class Queue:
    def __init__(self):
        self.arr0 = []
        self.arr1 = []

    @property
    def l(self): return len(self.arr0)

    def q(self, val):
        self.arr0.append(val)

    def d(self):
        if self.arr1: return self.arr1.pop()
        if self.arr0:
            while self.arr0:
                self.arr1.append(self.arr0.pop())
            return self.arr1.pop()
        return None

q = Queue()
# build new queue
[q.q(s) for s in list("moin")]

def m():
    for _ in range(q.l): yield q.d()

def moin():
    return "".join(m())

if __name__ == "__main__":
    print(moin())
