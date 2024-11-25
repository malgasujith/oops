class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child1(Parent):
    def greet_child1(self):
        print("Hello from Child1!")

class Child2(Parent):
    def greet_child2(self):
        print("Hello from Child2!")

child1 = Child1()
child2 = Child2()
child1.greet()
child1.greet_child1()
child2.greet()
child2.greet_child2()
