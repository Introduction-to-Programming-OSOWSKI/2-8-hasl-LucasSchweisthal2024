#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    for i in range(0, len(w)):
        if "l" == w[i]:
            return True
    return False

print(hasL("e"))
