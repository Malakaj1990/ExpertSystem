
class FactContainer:
    def __init__(self):
        self.key = ""
        self.finalDecision = ""
        self.reasons = []
        self.confident = 0
        self.printable = False


    def printFactContainer(self):
        print("############################################")
        print(self.finalDecision)
        print("Because ")
        i = 1
        reasonsString = "";
        for reason in self.reasons:
            reasonsString += str(i) + "-" + reason + "\n"
            i = i+1
        print(reasonsString)
        print("############################################")