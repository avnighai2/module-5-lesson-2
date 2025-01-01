class rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def rectangleArea(self):
        return self.length*self.width
newRec = rectangle(12, 10)
print(newRec.rectangleArea())