from pyknow import *
import FactContainer


class ProjectManaer(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.FactsMap = {}

    @DefFacts()
    def _initial_action(self):
        yield Fact(initialization=False)

    ############## Questioning Unknowns #############################################################################
    @Rule(Fact(initialization=False))
    def askInitialQuestion(self):
        print("Hi Im You'r Assistant Project Manager\nWhats your problem")
        print("1 - Your Delivery Quality Getting low")
        print("2 - Your Delivery Getting low")
        print("3 - Your Budget not enough")

        selectedValue = input("Press the number to select one")
        if selectedValue == '1':
            self.declare(Fact(LowQuality=True))
        elif selectedValue == '2':
            self.declare(Fact(DeliveryGettingSlow=True))
        elif selectedValue == '3':
            self.declare(Fact(BudgetNotEniugh=True))
        else:
            print("Invalid Selection Please select again")
            self.askInitialQuestion()

    @Rule(OR(Fact(DeliveryGettingSlow=True), Fact(LowQuality=True)), NOT(Fact(PeopleAreUnhappy=W())))
    def getDetailsAboutPeople(self):
        print("Are there any reported conflicts between people")
        print("1 - Yes")
        print("2 - No")
        selectedValue = input("Press the number to select one")
        if selectedValue == '1':
            self.declare(Fact(ConflictsAmongPeople=True))
        elif selectedValue == '2':
            self.declare(Fact(ConflictsAmongPeople=False))

        print("Are your people working late")
        print("1 - Yes")
        print("2 - No")
        selectedValue = input("Press the number to select one")
        if selectedValue == '1':
            self.declare(Fact(WorkingLate=True))
        elif selectedValue == '2':
            self.declare(Fact(WorkingLate=False))

    @Rule(Fact(DeliveryGettingSlow=True), Fact(PeopleAreUnhappy=False))
    def getInformationAboutInfastructure(self):
        print("Are there any complains about infrastructure")
        print("1 - Yes")
        print("2 - No")
        selectedValue = input("Press the number to select one")
        if selectedValue == '1':
            self.declare(Fact(InfrastructureProblem=True))
        elif selectedValue == '2':
            self.declare(Fact(InfrastructureProblem=False))

    #################DesisionMakings###################################################################
    @Rule(Fact(ConflictsAmongPeople=True), Fact(WorkingLate=True))
    def isPeopleUnhappy(self):
        factContainer = FactContainer.FactContainer()
        factContainer.finalDecision = "Employees Are not Happy"
        factContainer.key = "PeopleAreUnhappy"
        factContainer.reasons.append("There are conflict among people")
        factContainer.reasons.append("People are working late")
        factContainer.printable = True
        self.FactsMap[factContainer.key] = factContainer
        self.declare(Fact(PeopleAreUnhappy=True))

    @Rule(OR(Fact(ConflictsAmongPeople=False), Fact(WorkingLate=False)))
    def peopleAreHappy(self):
        self.declare(Fact(PeopleAreUnhappy=False))


    @Rule(Fact(ConflictsAmongPeople=True))
    def conflictAmongPeople(self):
        factContainer = FactContainer.FactContainer()
        factContainer.finalDecision = "Do Team building activity to improve spirit"
        factContainer.key = "DoTeamBuilding"
        factContainer.reasons.append("There are conflict among people")
        factContainer.printable = True
        self.FactsMap[factContainer.key] = factContainer
        self.declare(Fact(DoTeamBulding=True))

    @Rule(Fact(DeliveryGettingSlow=True), Fact(PeopleAreUnhappy=False), Fact(InfrastructureProblem=True))
    def badInfrastructure(self):
        factContainer = FactContainer.FactContainer()
        factContainer.finalDecision = "You need to upgrade your infrastructure"
        factContainer.key = "UpgradeInfarstructure"
        factContainer.reasons.append("Delivery Getting Slow")
        factContainer.reasons.append("People are happy")
        factContainer.reasons.append("There are complains about slow infrastructure")
        factContainer.printable = True
        self.FactsMap[factContainer.key] = factContainer
        self.declare(Fact(UpgradeInfarstructure=True))

    @Rule(Fact(DeliveryGettingSlow=True), Fact(PeopleAreUnhappy=False), Fact(InfrastructureProblem=False))
    def processNotGood(self):
        factContainer = FactContainer.FactContainer()
        factContainer.finalDecision = "Need to review current process. Improve your process"
        factContainer.key = "BadProcess"
        factContainer.reasons.append("Delivery Getting Slow")
        factContainer.reasons.append("People are happy")
        factContainer.reasons.append("Infrastructure is working fine")
        factContainer.printable = True
        self.FactsMap[factContainer.key] = factContainer
        self.declare(Fact(UpgradeInfarstructure=True))