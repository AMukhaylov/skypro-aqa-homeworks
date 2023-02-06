class Smartphone:
    def __init__(self, mark, model, number):
        self.mark = mark
        self.model = model
        self.number = number

    def say_smartphone(self):
        print(str(self.mark), str(self.model), str(self.number))

    def say_Mark(self):
        print("Марка", self.mark)

    def say_Model(self):
        print("Модель", self.model)

    def say_Number(self):
        print("Номер", self.number)