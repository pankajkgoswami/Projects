class Arrays(object):
    
    def __init__(self):
        self.array_length=0
    
    def reverseArray(self,length,myArray=[]):
        array_length=length
        if array_length%2==0:
            for i in range(0,int(array_length/2)):
                temp = myArray[int((array_length-1-i))]
                myArray[int((array_length-1-i))]=myArray[i]
                myArray[i]=temp
        else:
            for i in range(0,int((array_length+1)/2)-1):
                temp = myArray[int((array_length-1-i))]
                myArray[int((array_length-1-i))]=myArray[i]
                myArray[i]=temp
    
        for i in range(0,array_length):
            print(myArray[i])