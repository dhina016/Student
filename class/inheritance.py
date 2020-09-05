'''single inheritance'''
class CAT(): #parent
    def sound(self):
        print('meow')

class DOG():  # child
    def sound(self):
        print('bow')

animal1 = CAT()
animal2 = DOG()
animal1.sound()
animal2.sound()

'''multilevel inheritance'''
# class A():
#     def parent(self):
#         print('parent')

# class B(A):
#     def child(self):
#         print('child')

# class C(B):
#     def grandchild(self):
#         print('grand child')

# child1 = C()
# child1.parent()
# child1.child()
# child1.grandchild()


'''hierarchical inheritance'''

# class A():
#     def parent(self):
#         print('parent')

# class B(A):
#     def child1(self):
#         print('child1')

# class C(A):
#     def child2(self):
#         print('child2')

# child1 = B()
# child2 = C()
# child1.parent()
# child1.child1()
# child2.parent()
# child2.child2()

'''multiple inheritance'''

# class A():
#     def parent1(self):
#         print('parent1')

# class B():
#     def parent2(self):
#         print('parent2')

# class C(A, B):
#     def child(self):
#         print('child')

# child = C()
# child.parent1()
# child.parent2()
# child.child()


'''hybrid inheritance'''
# class A():
#     def parent(self):
#         print('parent')

# class B(A):
#     def child1(self):
#         print('child1')

# class C(A):
#     def child2(self):
#         print('child2')

# class D(B, C):
#     def grandchild(self):
#         print('grandchild')

# child1 = B()
# child1.parent()
# child1.child1()
# child2 = C()
# child2.parent()
# child2.child2()
# grandchild = D()
# grandchild.parent()
# grandchild.child1()
# grandchild.child2()
# grandchild.grandchild()