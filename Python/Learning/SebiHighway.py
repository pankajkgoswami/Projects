import sys
#in_data=map(str,input().split())
in_data = map(int,sys.stdin.readline().split())
#in_data = [str(x) for x in sys.argv[1:]]
no_of_test_cases = int(in_data[0])
print(no_of_test_cases)
Cases=in_data[1:]
j=0
val=[0]
for i in Cases:
    if((int(i)+1)%5==0):
        j=j+1
    val[j].append=Cases[i]
    
for k in val:
    print(val[k])

#no_of_test_cases = int(input())
#SeatNo=[]

#for i in range(no_of_test_cases):
#    data = int(input())
#    SeatNo.append(data)

