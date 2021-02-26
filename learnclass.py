class LivingBeing:
    bookOfTheLiving = []
    bookOfTheDead = []
    lbID = None

    def __init__(self, lbID):
        if lbID is None:
            lbID = 0
        else:
            lbID += 1
        self.bookOfTheLiving.append(lbID)
        print('Born ', lbID)

    def __del__(self, lbID):
        self.bookOfTheDead.append(lbID)

class Human(LivingBeing):
    def __init__(self, mname):
        self.name = mname

for i in range(10):
    x = Human(i)

print(LivingBeing.bookOfTheLiving)