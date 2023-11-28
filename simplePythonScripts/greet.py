class ComplexNum:
    def __init__(self, r=0, i=0):
        self.real = r
        self.img = i

    def get_data(self):
        print(f'{self.real} + {self.img}i')

complex1 = ComplexNum(1,3 )
v = complex1.get_data()

complex2 = ComplexNum(2)
complexAttri =5
print(complex2.real, complex2.img, complexAttri)