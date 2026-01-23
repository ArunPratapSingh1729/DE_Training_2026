class A:
    def method_a(self):
        print("Method from class A")


class B(A):             
    def method_b(self):
        print("Method from class B")


class C:
    def method_c(self):
        print("Method from class C")


class D(B, C):          
    def method_d(self):
        print("Method from class D")


d = D()

d.method_a()   
d.method_b()   
d.method_c()   
d.method_d()   
