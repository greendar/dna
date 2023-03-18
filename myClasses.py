import random

class Person:
    def __init__(self, mother, father):
        self.mother = mother
        self.father = father
        self.genes = mother.add(father)
        self.generation = self.mother.generation + 1

class Traits:
    """
    List in Order (in pairs)
    Hair, Hair Legacy, Nose, Nose Legacy     THIS WILL CHANGE
    QTRD qtrd

    Have not included any code that indicates gender.
    """

    def __init__(self, traitInput):
    # Initialize traitList
        self.traitList = []
        self.traitListIn = [traitInput[0:2], traitInput[2:4], traitInput[4:6], traitInput[6:]]
        for pair in self.traitListIn:
            self.traitList.append(self.traitOrder(pair))

    def traitOrder(self, traitsIn):
        # to determine first or second position in the pair
        trait1 = traitsIn[0]
        trait2 = traitsIn[1]
        if trait1.isupper() and trait2.isupper() or trait1.islower() and trait2.islower():
            roll = random.random()
            if roll < 0.5:
                return trait1 + trait2
            else:
                return trait2 + trait1
        if trait1.isupper() and trait2.islower():
            roll = random.random()
            if roll < 0.7:
                return trait1 + trait2
            else:
                return trait2 + trait1
        if trait2.isupper() and trait1.islower():
            roll = random.random()
            if roll < 0.7:
                return trait2 + trait1
            else:
                return trait1 + trait2
    
    def show(self):
        for trait in self.traitList:
            print(trait, end='-')
        print()

    def makeHeir(self, other):
        temp = ''
        heirTraitList = [0,0,0,0]
        for i in range(len(self.traitList)):
            heirTraitList[i] = self.traitList[i] + other.traitList[i]
        for trait in heirTraitList:
            temp += self.passedTraits(trait)
        return temp

''' Depricated
    def add(self, other): # NEED to change for larger sets
        for i in range(len(self.traitList)):
            self.heirTraitList[i] = self.traitList[i] + other.traitList[i]
'''

    def passedTraits(self, traitsIn):
        '''
        First iteration.
        To do:
        -change so that it is a weighted choice
        -decide whether to fix the possible duplication error or make it a feature
        '''
        domTraits = []
        nDomTraits = []
        for trait in traitsIn:
            if trait.isupper():
                domTraits.append(trait)
            else:
                nDomTraits.append(trait)
        if domTraits != 0:
            domTrait = random.choice(domTraits)
        else:
            domTrait = random.choice(nDomTraits)
        if nDomTraits != 0:
            nDomTrait = random.choice(nDomTraits)
        else:
            nDomTrait = random.choice(domTraits) #may end up with an error of duplication
        return self.traitOrder(domTrait+nDomTrait)
        



if __name__ == "__main__":
    for i in range(5):
        a = Traits('qTRdtRdQ')
        b = Traits('DrQtTqRd')
        print('Show a')
        a.show()
        print('Show b')
        b.show()
        print('Show heir', end='\n                  ')
        c = Traits(a.makeHeir(b))
        c.show()



    
    