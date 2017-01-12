''' 
@author: Pankaj Goswami
Link of problem: https://www.hackerrank.com/challenges/s10-quartiles
'''
import sys
no_of_test_cases = int(input())
data_values = (input().split())
int_data_values=[]
n = no_of_test_cases
sum_med = 0


for i in range(n):
    int_data_values.append(int(data_values[i]))
    
# Sorting the array to get median
int_data_values.sort()

def median_calc(input_data):
    length_arr = len(input_data)
    data_val = input_data
    even_elements=(length_arr%2==0)
    # Calculating Median
    if even_elements:
        sum_med=(data_val[int(length_arr/2 -1)])+ (data_val[int(length_arr/2)])
    else:
        sum_med=(data_val[int((length_arr)/2)])
    
    if even_elements:
        med=sum_med/2
    else:
        med=sum_med
    
    return(round(med,1))



if (n%2==0):
    mid=int(n/2)
else:
    mid=int((n-1)/2)

Q1=(median_calc(int_data_values[:mid]))
Q2=(median_calc(int_data_values))
Q3=(median_calc(int_data_values[(mid):]))
print(Q1)
print(Q2)
print(Q3)