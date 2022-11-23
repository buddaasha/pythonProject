class check():
    def __init__(self):
        print("Address of self = ",id(self))
  
obj = check()
print("Address of class object = ",id(obj))

class car():
    def __init__(self,model,color):
        self.model = model
        self.color = color
    
    def show(self):
        print("Model is", self.model)
        print("color is",self.color)




