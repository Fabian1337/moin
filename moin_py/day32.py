def check_right(m, r, c, word):
    word_len = len(word)
    row_len = len(m[0])
    if word_len != row_len - c: return False
    for c1, c2 in zip(word, (m[r][i] for i in range(c, row_len))):
        if c1 != c2: return False
    return True

def check_down(m, r, c, word):
    word_len = len(word)
    col_len = len(m)
    if word_len != col_len - r: return False
    for c1, c2 in zip(word, (m[i][c] for i in range(r, col_len))):
        if c1 != c2: return False
    return True

def search(m, word):
    for r, row in enumerate(m):
        for c, _ in enumerate(row):
            if check_right(m, r, c, word): return True
            if check_down(m, r, c, word): return True
    return False

m = [
    ["M", "D", "M", "N", "A", "N", "M", "D"],
    ["O", "P", "O", "P", "T", "I", "E", "V"],
    ["A", "X", "I", "B", "C", "O", "P", "B"],
    ["M", "A", "N", "I", "B", "A", "F", "C"]
    ]

def moin():
    return "moin" if search(m, "MOIN") else "404 NO MOIN FOUND"

if __name__ == "__main__":
    print(moin())
