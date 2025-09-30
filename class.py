#Function Defining inside a class

class counting: #Function defined insdie a class
    n=0

    def cnt(self):
        self.n=self.n +1
        print("Counted",self.n)

c=counting()

c.cnt()
c.cnt()