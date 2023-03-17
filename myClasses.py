class Traits:
    """
    List in Order (in pairs)
    Hair, Hair Legacy, Nose, Nose Legacy
    QZWXqzwx
    """
    # The percentage a dominant trait will be chosen over non-dominant
    dominantTraitPerc = 0.75

    # A weighting to show the likelyhood of
    # trait to be chosen over another of similar dominance
    dominantQPerc = 0.5
    dominantZPerc = 0.5
    dominantWPerc = 0.5
    dominantXPerc = 0.5

    def __init__(self):
    # Initialize traitList
        self.traitList = [0,0,0,0]
        self.heirTraitList = [0,0,0,0]

    def show(self):
        for trait in self.traitList:
            print(trait)

    def showHeir(self):
        for trait in self.heirTraitList:
            print(trait)

    def load(self, userInput):
        if userInput == '':
            userInput = input("Enter Traits Here (8 letters QZWXqzwx)")
        self.traitList[0] = userInput[0:2]
        self.traitList[1] = userInput[2:4]
        self.traitList[2] = userInput[4:6]
        self.traitList[3] = userInput[6:]

    def add(self, other):
        self.heirTraitList[0] = self.traitList[0] + other.traitList[0]
        self.heirTraitList[1] = self.traitList[1] + other.traitList[1]
        self.heirTraitList[2] = self.traitList[2] + other.traitList[2]
        self.heirTraitList[3] = self.traitList[3] + other.traitList[3]





    # Replicate Problem
        '''
    We have 4 genes   eg QwZx and need to come up with
    a way to choose 1
    '''



if __name__ == "__main__":
    a = Traits()
    b = Traits()
    a.load('QZWXxwzq')
    b.load('WxqZqzWX')
    a.add(b)
    a.showHeir()

    
    