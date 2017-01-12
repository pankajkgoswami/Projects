''' 
@author: Pankaj Goswami
Link of problem: https://www.hackerrank.com/challenges/s10-weighted-mean
'''
import sys
no_of_test_cases = int(input())
data_values = (input().split())
data_weights = (input().split())
int_data_values=[]
n = no_of_test_cases
total=0
weight_total=0

for i in range(n):
    total=total+int(data_values[i])*int(data_weights[i])
    weight_total = weight_total+int(data_weights[i])
    
weighted_mean = round(total/weight_total,1)

print(weighted_mean)