
def moin():
    return "".join([elem[(idx // 3) % 2] for idx, elem in enumerate(zip(["x", "<", "m", "m", "o", "n", 'd', 'k', '>', '3', '5', 'l'], ['y', 'x', '3', 'o', 'i', 'n', 'g', 'h', 'i', '7', '-', 'j']))][2:6])

if __name__ == "__main__":
    print(moin())