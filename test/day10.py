ascii_moin = '''
MMMM    MMMM  oOOOOOOOOOOo  III  NN     NN
MM  MMMM  MM  oO        Oo       NNNN   NN
MM   MM   MM  oO   oO   Oo  III  NN Nn  NN
MM   MM   MM  oO        Oo  III  NN   N NN 
MM        MM  oOOOOOOOOOOo  III  NN    NNN
'''

def arrange_moin(arr):
    i, m, n, o = arr
    return [m, o, i, n]

def moin():
    moin_filter = ["n", "i", "o", "m"]
    return "".join(arrange_moin(sorted(set(list(filter(lambda x: x in moin_filter, ascii_moin.lower()))))))

if __name__ == "__main__":
    print(moin())