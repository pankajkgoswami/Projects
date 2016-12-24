t = int(input())
while t!=0 :
    t = t - 1
    counter=0
    inputs = input().split()
    l=[]
    while inputs:
        l.append(inputs[:1])
        inputs=inputs[1:]
    
    strg=inputs[0]
    print(strg[0])
        
    for i in range(len(l)):
        if l[i]=='<':
            l[i]='>'
        elif l[i]=='>':
            l[i]='<'
        else:
            l[i]=l[i]
        print(l[i])
    
    for j in range(len(l)):
        print(l[j])
        #if inputs[i]=='>' & inputs[i+1]=='<':
        #    counter=counter+1
    print(counter)
        