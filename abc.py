
from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def sound(self):
        pass

    
    def sleep(self):
        print("This animal is sleeping.")

class D(A):

    def sound(self):
        print("Bark!")

class C(Animal):

    
    def sound(self):
        print("Meow!")

dog = D()
dog.sound() 
dog.sleep()  

cat = C()
cat.sound()  
cat.sleep()