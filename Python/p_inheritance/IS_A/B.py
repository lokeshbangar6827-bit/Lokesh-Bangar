from A import A
class B(A):
    
    def abc(self):
        print("Hello abc")
    
    def __init__(self):
        print("def con of B class")
    
obj=B()
print(B.mro())  #method resolution order...