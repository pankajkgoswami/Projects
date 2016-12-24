from Learning.Class import Run
n1 = Run()

n1.insert(10)
n1.insert(6)
n1.insert(5)
n1.insert(7)
n1.insert(15)
n1.insert(36)
n1.insert(-5)
n1.insert(22)

n1.traverseInOrder()

print("Minimum")
print(n1.getMin())