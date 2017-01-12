''' 
@author: Pankaj Goswami
Link of problem: https://www.hackerrank.com/challenges/s10-standard-deviation/tutorial
'''
import sys
from math import sqrt
no_of_test_cases = int(input())
data_values = (input().split())
int_data_values=[]
n = no_of_test_cases
Total=0
squared_diff_total=0

for i in range(n):
    Total=Total+int(data_values[i])
    int_data_values.append(int(data_values[i]))

mean=Total/n

for i in range(n):
    squared_diff_total=squared_diff_total+(int((data_values[i]))-mean)**2
    
variance=squared_diff_total/n
std_var=round(sqrt(variance),1)
print(std_var)
    
