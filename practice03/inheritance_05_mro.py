# ============================================================================
# TOPIC 5: Inheritance chain and method resolution order (MRO)
# ============================================================================

class A:
    def method(self):
        print("Method from class A")

class B(A):
    def method(self):
        print("Method from class B")

class C(A):
    def method(self):
        print("Method from class A")

class D(B, C):
    pass

d = D()
d.method()  # Shows MRO - B is checked before C

print(f"MRO for class D: {[cls.__name__ for cls in D.__mro__]}")









