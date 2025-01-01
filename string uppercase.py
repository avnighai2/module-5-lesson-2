class IOSstring():
    def __init__(self):
        self.str1 = ""
    def getString(self):
        self.str1 = input("Enter String:")
    def printString(self):
        print("Result is :", self.str1.upper())

str1 = IOSstring()
str1.getString()
str1.printString()