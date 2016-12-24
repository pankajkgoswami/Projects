from Kruskal.DisjoinSet import DisjoinSet
class Algorithm(object):
    
    def constructSpanningTree(self,vertexList,edgeList):
        disjoinSet = DisjoinSet(vertexList)
        spanningTree=[]
        
        edgeList.sort()
        
        for edge in edgeList:
            u=edge.startVertex
            v=edge.targetVertex
            
            if disjoinSet.find(u.parentNode) is not disjoinSet.find(v.parentNode):
                spanningTree.append(edge)
                disjoinSet.union(u.parentNode, v.parentNode)
        
        for edge in spanningTree:
            print(edge.startVertex.name,"-",edge.targetVertex.name)