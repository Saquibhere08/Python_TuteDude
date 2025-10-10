#Multi-Level Inheritance


class A:
    def state_1(self):
        print("State 1 present")
    
    def state_2(self):
        print("State 2 present")

    def state_3(self):
        print("State 3 present")


class B(A): #class attributes inherited from another class
    def state_4(self):
        print("State 4 present")

    def state_5(self):
        print("State 5 present")

class C(B): #Multi-Level Inheritance
    def state_6(self):
        print("State 6 present")

c=C() #Multi-Level Inheritance
c.state_1()