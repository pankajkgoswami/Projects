from BinarySearchTreeDS.BinarySearchTree import BST;

bst = BST()

bst.insert(10)
bst.insert(1)
bst.insert(4)
bst.insert(7)
bst.insert(2)
bst.insert(-5)
bst.insert(15)
bst.insert(18)
bst.insert(14)
bst.insert(17)

print("The current order is ")
bst.traverseInOrder()


bst.remove(18)

print("The New order is ")

bst.traverseInOrder()

print(bst.getMin())

print(bst.getMax())
