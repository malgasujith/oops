class parent:
    result = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def main(self):
        res1 = self.a + self.b
        print(f"parent class {res1}")
class child(parent):
    def __init__(self,c, d, a, b):
        super().__init__(a,b)
        self.c = c
        self.d = d
    def method(self):
        res = self.c + self.d
        res2 = self.a + self.b + res
        print(f"derived class {res2}")

a = 2
b = 3
c = 5
d = 5
obj = child(c,d,a,b)
obj.method()
obj.main()
