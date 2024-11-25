class Parent1:
    def greet1(self):
        print("Hello from Parent1!")

class Parent2:
    def greet2(self):
        print("Hello from Parent2!")

class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from Child!")


child = Child()
child.greet1()
child.greet2()
child.greet_child()
