from DepthFirstSearch.Node import Node
import DFS

node1=Node("A")
node2=Node("B")
node3=Node("C")
node4=Node("D")
node5=Node("E")

node1.adjanciesList.append(node2)
node1.adjanciesList.append(node3)
node2.adjanciesList.append(node4)
node4.adjanciesList.append(node5)

DFS.dfs(node1)