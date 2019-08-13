import datetime

def moin():
    return "moin" if(datetime.datetime.now()) else None # wie wir alle wissen egal wann wird moin gesagt!


if __name__ == "__main__":
    print(moin())

