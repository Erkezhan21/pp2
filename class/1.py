class MyClass:
    s = ""
    def getString(self):
        self.s = input()
        # print("I'm", self.att1)
        # print("I'm", self.att2)
    def printString(self):
        print(self.s.upper())

qwerty = MyClass()

qwerty.getString()
qwerty.printString()
