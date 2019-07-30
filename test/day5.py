import string

def moin():
    return 'NIOMnienellathcsneuwnaibaf'[::-1].translate(str.maketrans('','',string.ascii_lowercase)).lower()

if __name__ == "__main__":
    print(moin())
