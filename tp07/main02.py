
class A:
    def __init__(self, valA):
        self.valA = valA
        print(f"A def __init__(self, {valA}):")

    def the_method(self):
        print("the_method A",self.valA)
        
class B(A):
    def __init__(self, valB):
        super().__init__(valB)
        print(f"B def __init__(self, {valB}):")

    def the_method(self):
        print("the_method B",self.valA)


class C(A):
    def __init__(self, valC):
        super().__init__(valC)
        print(f"C def __init__(self, {valC}):")

    def the_method(self):
        print("the_method C",self.valA)
class D(B,C):
    def other_method(self):
        print("other_method C")
        # print(C.__mro__)
        super().the_method()
        # super(B,self).the_method()
        super(C,self).the_method()
        
        
        
def main():
    print(D.mro())
    d = D(2)
    s = super(B,d)
    print(s)

if __name__=='__main__':
    main()
        

        
        
        


