import sys
class Edge(object):
    
    def __init__(self,weight,startVertex,targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Vertex(object):
    
    def __init__(self,name):
        self.name=name
        #self.visited=False
        self.predecessors=[]
        self.minDistance=sys.maxsize
        #print("appended:"+name)

class Algorithm(object):
    #print("Algorithm Started")    
    def minDist(self,vertexList,edgeList):
        length=len(vertexList)
        #print("Length: "+str(length))
        minDistance=int(vertexList[length-1].name)
        #print("First Min"+str(minDistance))
        cnode=sys.maxsize
        
        pred=length
        for i in reversed(range(len(vertexList))):
            node=vertexList[i]
            
            #print("value of i "+str(i))
            if i >= cnode:
                continue
            
            #print("Node pred length: "+str(len(node.predecessors)))
            
            for j in range(len(node.predecessors)):
                #print("node pred value: "+node.predecessors[j])
                if int(node.predecessors[j]) < pred:
                    pred=int(node.predecessors[j])
                    #print("I am : "+str(pred))
                    cnode=int(node.predecessors[j])
            
            minDistance=minDistance*pred
            #print("Min Distance : "+str(minDistance)) 
        
        print(minDistance)
        
INP = input().split(" ")
No_vertices = int(INP[0])
K = int(INP[1])
nodeList=[]
edgeList=[]
#print(No_vertices)
#while No_vertices != 0:
No_vertices = No_vertices - 1
inputs = input().split()
for i in range(len(inputs)):
    nodeList.append(Vertex(inputs[i]))
    
# To populate the Edge    
for j in range(len(inputs)-1):
    #print("Edge details:")
    for k in range(K):
        if (j+k+2)>len(inputs):
            continue
        edge=Edge(int(nodeList[j+k+1].name),nodeList[j],nodeList[j+k])
        edgeList.append(edge)
        #nodeList[j+k+1].Vertex.predecessors.append[nodeList[j]]
        currentNode=nodeList[j+k+1]
        predecessor=nodeList[j].name
        currentNode.predecessors.append(predecessor)
        #print(nodeList[j+k+1].predecessors.append[predecessor])
        #print(currentNode.predecessors)
        #print(edge.weight)
        
algorithm = Algorithm()
algorithm.minDist(nodeList, edgeList)

