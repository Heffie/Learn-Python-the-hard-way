class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, before parent altered")
        super(Child, self).altered()
        print("CHILD, after parent altered")

parent = Parent()
child = Child()

parent.altered()
child.altered()
