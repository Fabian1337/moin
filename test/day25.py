m = '''
    ____
 __/  |_\_
|  _     _``-.
'-(_)---(_)--'
'''
i = "nie"
n = "hcs"
o = "hüfrer"

def moin():
    return "".join((chr(len(m)*2+len(o)+1), chr(int(int((ascii(o[3:]+o[:3])[::-1])[1:3], 16)/2)- (1<<4) + 1), i[1], chr(ord(n[2])-5)))

if __name__ == "__main__":
    print(moin())