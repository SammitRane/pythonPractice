class A:
    def __init__(self):
        print("Class A constructor")
        
class B:
    def __init__(self):
        print("Class B constructor")
        
class C (B,A):
    def __init__(self):
        super().__init__()
        
        
obj = C()
