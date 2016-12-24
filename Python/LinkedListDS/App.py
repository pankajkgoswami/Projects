from LinkedListDS.LinkedList import LinkedList;

linkedlist = LinkedList();

linkedlist.insertEnd(12);
linkedlist.insertEnd(13);
linkedlist.insertEnd(15);
linkedlist.insertEnd(1);
linkedlist.insertEnd(122);
linkedlist.insertEnd(32);
print('Existing List');
linkedlist.traverseList();

linkedlist.remove(1);
print('New List');
linkedlist.traverseList();