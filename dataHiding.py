class simple:
    def __init__(self):
        self.__value_1=1
        self.value_2=2

    def __A1_(self):
        print("applee")
    
    def _B2_(self):
        print("ball")

s=simple()

print(dir(s))

print(s._simple__value_1)

'''data hiding: Data hiding involves restricting direct access to class members (typically data fields or variables) from outside the class. It is commonly achieved by declaring data members as private, making them accessible only through special public methods like getters (to read data) and setters (to modify data after appropriate checks). This protects sensitive
 information from corruption, hacking, or accidental changes
'''