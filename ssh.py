
class Addition():
    first = 0
    second = 0
    answer = 0
    def __init__(self,f,s):
        self.first = f
        self.second = s
    def add(self):
       self.answer = self.first+self.second
       return self.answer
    def display(self):
        print(self.first)
        print(self.second)
        print(self.answer)
    def big(self):
        if (self.answer == 10):
            print("i is 10")
        else:
            print ("i is not present")

obj = Addition(100,200)
obj.add()
obj.display()
obj.big



   
        
