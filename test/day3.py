import string, re

def moin():
    imno = list(filter(None, re.sub(r'[a-h,j-l,p-z]','', string.ascii_lowercase[:27])))
    return ''.join((imno[1], imno[3], imno[0], imno[2]))

if __name__ == "__main__":
    print(moin())
