class Maze:
    FOUND = {}

    def __init__(self):
        self.steps = 0
        self.moin_maze = [
            ["x", "|", "x", "x", "x", "i"],
            ["x", "|", "x", "|", "x", "x"],
            ["n", "|", "o", "|", "x", "x"],
            ["x", "|", "x", "|", "x", "x"],
            ["x", "|", "x", "|", "x", "x"],
            ["x", "x", "x", "|", "x", "m"],
        ]

    def search(self, x, y, s):
        if self.moin_maze[x][y] == s:
            self.FOUND[s] = (x, y, self.steps)
            return True
        elif self.moin_maze[x][y] == "|": return False
        elif self.moin_maze[x][y] == "X": return False 
        self.moin_maze[x][y] = "X"
        self.steps += 1

        if ((x < len(self.moin_maze)-1 and self.search(x+1, y, s))
            or (y > 0 and self.search(x, y-1, s))
            or (x > 0 and self.search(x-1, y, s))
                or (y < len(self.moin_maze)-1 and self.search(x, y+1, s))):
            return True

        return False

[Maze().search(0, 0, s) for s in list("moin")]
def mul(l): return eval(str(l).replace(',', '*'))

def moin():
    return "".join((chr((mul(Maze.FOUND["m"]) >> 2) - 16), chr((mul(Maze.FOUND["o"]) << 1) + (1 << 5) - 1), chr(Maze.FOUND["i"][1]*Maze.FOUND["i"][2]-Maze.FOUND["m"][2]), chr((Maze.FOUND["n"][0]**Maze.FOUND["m"][0] << 2)-18)))

if __name__ == "__main__":
    print(moin())
