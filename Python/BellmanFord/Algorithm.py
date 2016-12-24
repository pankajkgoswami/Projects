class Algorithm(object):
    
    HAS_CYCLE=False
    
    def calculateShortestPath(self,vertexList,edgeList,startVertex):
        
        startVertex.minDistance=0
        
        for i in range(0,len(vertexList)-1):
            for edge in edgeList:
                
                u=edge.startVertex
                v = edge.endVertex
                newDistance=u.minDistance+edge.weight
                
                if newDistance<v.minDistance:
                    v.minDistance=newDistance
                    v.predecesser=u
                    
        
        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative Cycle detected")
                Algorithm.HAS_CYCLE=True
                return
    def hasCycle(self,edge):
        if edge.startVertex.minDistance + edge.weight < edge.endVertex.minDistance:
            return True
        else:
            return False
    
    def getShortestPath(self,targetVertex):
        print("Shortest path to Target Vertex: ",targetVertex.minDistance)
        
        node=targetVertex
        
        while node is not None:
            print("%s ->" %node.name)
            node = node.predecesser
        