class Base:
    def greet_base(self):
        print("Hello from Base!")

class Parent1(Base):
    def greet_parent1(self):
        print("Hello from Parent1!")

class Parent2(Base):
    def greet_parent2(self):
        print("Hello from Parent2!")

class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from Child!")


child = Child()
child.greet_base()
child.greet_parent1()
child.greet_parent2()
child.greet_child()
