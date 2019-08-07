ascii_moin = '''
MMMM    MMMM  oOOOOOOOo  III   NN       NN
MM  MMMM  MM  oO                Oo        NNN    NN
MM     MM      MM  oO   oO        Oo  III   NN Nn  NN
MM     MM      MM  oO                Oo  III   NN   N  NN 
MM                  MM  oOOOOOOOo   III   NN     NNN
'''

def arrange_moin(arr):
    i, m, n, o = arr
    return [m, o, i, n]

def moin():
    moin_filter = ["n", "i", "o", "m"]
    return "".join(arrange_moin(sorted(set(filter(lambda x: x in moin_filter, ascii_moin.lower())))))

if __name__ == "__main__":
    print(moin())