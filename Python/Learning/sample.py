import sys
in_data = [int(x) for x in sys.argv[1:]]
#print(in_data)

array_length=in_data[0]
myArray=in_data[1:]
#print(myArray)

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
            #return myArray[i]

