INP = input().split(" ")
NF = int(INP[0])
NP = int(INP[1])
SP_F = input().split(" ")
post_priority=[]
while NP!=0 :
    NP = NP - 1
    inputs = input().split()
    f = inputs[0]
    p = inputs[1]
    c = inputs[2]
    priority = 0
    if f in SP_F:
        priority=1 
    post_priority.append(str(priority)+str(p).zfill(5)+'-'+c)

post_priority.sort(key=None, reverse=True)

for i in range(len(post_priority)):
    pt=post_priority[i]
    print(pt[7:])