from itertools import product
import random
#import timeit

def moin():
    chars = 'abcdefghijklmnopqrstuvvxyz'

    for length in range(5):
        to_attempt = product(random.sample(chars, len(chars)), repeat=length)
        for attempt in to_attempt:
            if ''.join(attempt) == "moin":
                return ''.join(attempt)

if __name__ == "__main__":
    print(moin())
    #print(timeit.timeit(moin, number=100)) # 3.1959122 vllt. ist ja jemand schneller xD