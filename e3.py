import random

mnames = ['Alpha', 'Bravo', 'Charley', 'Delta', 'Echo', 'Foxtrot', 'Golf']

class LivingBeing:
    bookOfTheLiving = dict()
    spieces = 'Living Being'

    def __init__(self, lID, name):
        self.sID = lID
        self.name = name
        self.bookOfTheLiving[self.sID] = self.name
        print("Born", self.sID, self.name)
    
for i in range(10):
    somename = mnames[random.randint(0, 6)]
    being = LivingBeing(i, somename)
    if i == 9:
        print(being.bookOfTheLiving)