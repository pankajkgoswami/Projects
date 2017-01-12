import sys
no_of_test_cases = int(input())
data_values = (input().split())
int_data_values=[]
n = no_of_test_cases
dictmode={}

for i in range(n):
    if data_values[i] in dictmode.keys():
        dictmode[data_values[i]]=dictmode[data_values[i]]+1
    else:
        dictmode[data_values[i]]=1

cnt=1
ky=str(-sys.maxsize - 1)
for key, value in dictmode.items():
    #print(value)
    if value>=cnt:
        if value==cnt:
            if int(key)<int(ky):
                cnt=value
                ky=key
        else:
            cnt=value
            ky=key

print(ky)
