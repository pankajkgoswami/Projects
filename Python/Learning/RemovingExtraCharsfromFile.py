import os,shutil 
for filename in os.listdir('E:\\Work\\Learning\\Python\\Videos from Youtube\\Machine Learning\\Deep Learning With Tensorflow'):
    newname=filename
    if len(newname)>35:
        print(newname[:-16])
        #head=newname[0:4]
        #new_name=(newname[0:(newname[1:].find(head))])+".mp4"
        new1_name=newname[:-16]
        #print(new_name)
        #shutil.move('E:\\Work\\Learning\\Python\\Videos from Youtube\\Machine Learning\\'+filename,'E:\\Work\\Learning\\Python\\Videos from Youtube\\Machine Learning\\'+new_name+".mp4")
        shutil.move('E:\\Work\\Learning\\Python\\Videos from Youtube\\Machine Learning\\Deep Learning With Tensorflow\\'+filename,'E:\\Work\\Learning\\Python\\Videos from Youtube\\Machine Learning\\Deep Learning With Tensorflow\\'+new1_name+".mp4")
    else:
        print(newname)