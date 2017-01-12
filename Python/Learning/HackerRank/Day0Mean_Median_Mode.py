''' 
@author: Pankaj Goswami
Link of problem: https://www.hackerrank.com/challenges/s10-basic-statistics
'''
import sys
no_of_test_cases = int(input())
data_values = (input().split())
int_data_values=[]
n = no_of_test_cases
sum_mean=0
sum_med = 0
even_elements=(n%2==0)

for i in range(n):
    sum_mean=sum_mean+int(data_values[i])
    int_data_values.append(int(data_values[i]))

mean=sum_mean/n
print(round(mean,1))
    
# Sorting the array to get median
int_data_values.sort()

# Calculating Median        
if even_elements:
    sum_med=(int_data_values[int(n/2 -1)])+ (int_data_values[int(n/2)])
else:
    sum_med=(int_data_values[int((n+1)/2)])
        
if even_elements:
    med=sum_med/2
else:
    med=sum_med

print(round(med,1))

dictmode={}

for i in range(n):
    if data_values[i] in dictmode.keys():
        dictmode[data_values[i]]=dictmode[data_values[i]]+1
    else:
        dictmode[data_values[i]]=1

cnt=1
ky=str(sys.maxsize)
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
