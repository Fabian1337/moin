import pickle, base64

def moin():
    n = pickle.loads(base64.b64decode(b'gANdcQAoWAMAAABiZW5xAVgFAAAAaGVsZ2VxAlgGAAAAdm94ZWxzcQNYBgAAAGZhYmlhbnEEWAYAAABwYXNjYWxxBVgFAAAAY29zbW9xBmUu'))
    return "{}{}".format(n[-1][-2:], n[3][-3:].replace("a", ""))

if __name__ == "__main__":
    print(moin())
