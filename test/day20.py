def moin():
    try:
        text = input()
        if input() == "moin":
            return text
        else:
            raise Exception('moin')
    except Exception as e:
        return e


if __name__ == "__main__":
    print(moin())
