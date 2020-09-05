def checkFive(n):  #
    if n == 5:
        return True
    else:
        return False

def findLen(s): # get
    return (len(s))  # return

def strReverse(a):  #
    return (a[::-1])

def oddEven(n):
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'

string = input() # user input
length = findLen(string) # pass and returned value  string 6 checkFive true odd even
print(length)
if checkFive(length):  # checkFive(1)
    print(oddEven(length))
else:
    print('statement false')
print(strReverse(string))