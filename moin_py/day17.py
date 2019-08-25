import datetime

def moin():
    return "moin" if(datetime.datetime.now()) else "moin" # wie wir alle wissen egal wann wird moin gesagt auch wenn es keine zeit mehr gibt!

if __name__ == "__main__":
    print(moin())

