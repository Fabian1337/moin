class Node:
    mino = []
    def __init__(self, val):
        self.links = None
        self.rechts = None
        self.val = val

    def pre(self):
        self.mino.append(self.val)
        if self.links: self.links.pre()
        if self.rechts: self.rechts.pre()

def rev(n):
    if not n: return n    
    links = rev(n.links)
    rechts = rev(n.rechts)
    n.links, n.rechts = rechts, links
    return n

def moin():
    root = Node('m')                #...m..        
    root.links = Node('i')          # ./.\.
    root.rechts = Node('o') 	    #.i...o
    root.links.links = Node('n')    #/.....                    
    rev(root)                       #n.....
    root.pre()
    return "".join(root.mino) 

if __name__ == "__main__":
    print(moin())



