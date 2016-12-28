import os,shutil,re
for filename in os.listdir('E:\\Work\\Learning\\Python\\Videos from Youtube\\Machine Learning'):
    newname=filename
    p = re.search(r"(p.\d\d)-", newname)
    if p:
        nn =p.group()+newname
        shutil.move('E:\\Work\\Learning\\Python\\Videos from Youtube\\Machine Learning\\'+filename,'E:\\Work\\Learning\\Python\\Videos from Youtube\\Machine Learning\\'+nn)
    else:
        print(" Fname: ",newname) 