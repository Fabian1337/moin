wiki_moin = '''
From Wikipedia, the free encyclopedia

Moin, moi or mojn is a Low German, Frisian, High German (moin [moin] or Moin, [Moin])[1], Danish (mojn)[2] and Kashubian greeting from East Frisia, Southern Schleswig (including North Frisia and Flensburg), Bremen, Hamburg, Holstein, Mecklenburg-Vorpommern, the eastern and northern Netherlands and Southern Jutland in Denmark.
It means "hello" and, in some places, "goodbye".

Usage:
Moin is used at all times of day, not just in the morning (see Etymology section below).[3] The reduplicated form moin moin is often heard,[4] although some authors claim it is regarded by locals as tourists' usage.[5]

The German comic character Werner always greets with Moin. 
'''

def wcount(word):
    return wiki_moin.lower().count(word)

moin_dict = {
    "m": chr((wcount("moin")*wcount("moi")+wcount("mojn")*9)^1),
    "o": wiki_moin[wiki_moin.find("Usage:")+8:wiki_moin.find("Usage:")+9],
    "i": [i for i in list("Wikipedia") if i == "i"][0],
    "n": chr((sum(list(map(len, ([m for m in wiki_moin.lower() if m is "m"]))))<<2)+~17)
}

def moin():
    return "{m}{o}{i}{n}".format(**moin_dict)

if __name__ == "__main__":
    print(moin())