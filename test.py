def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


l = (1, 2 , 3)
print(multiplyList(l))

mu = lambda l: eval(str(l).replace(',','*'))
print(mu(l))