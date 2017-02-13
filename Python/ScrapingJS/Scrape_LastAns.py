import requests,os,csv
from bs4 import BeautifulSoup
counter = 0
def URLExtract(url,counter):
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(page.content, 'html.parser')
    soup1 = BeautifulSoup(page.content, 'html.parser')
    g_data=soup.find_all(id='content')
    #print(g_data)
    tt = str(g_data)
    targetFileName='temp.csv'
    finalfilex = 'ListofQues.txt'
    ansfilex='answers.txt'
    targetFolder=os.getcwd()
    # If the folder Does not exist it will be created
    if os.path.exists(os.path.join( targetFolder,'data')):
        csvfilex = os.path.join( targetFolder,'data',targetFileName)
        finalfile = os.path.join( targetFolder,'data',finalfilex)
        ansfile = os.path.join( targetFolder,'data',ansfilex)
    else:
        os.makedirs(os.path.join( targetFolder,'data'))
        csvfilex = os.path.join( targetFolder,'data',targetFileName)
        finalfile = os.path.join( targetFolder,'data',finalfilex)
        ansfile = os.path.join( targetFolder,'data',ansfilex)

    with open(csvfilex, 'w') as err_fname:
        err_fname.writelines(tt)
        #err_fname.write('\n')
    err_fname.close()
    
    num_lines = sum(1 for line in open(csvfilex))

    questionList=[]
    answerList=[]
    with open(csvfilex,'r') as filex:
        ques = ("Question: "+str(counter))
        questionList.append(ques)
        for line in filex :
            if "<p>" in line:
                line1=line.replace('<p>A ','')
                line2=line1.replace('<p>','')
                line3=line2.replace('</p>','')
                line4=line3.replace('<br/>','')
                line5=line4.replace('</u>','')
                line6=line5.replace('<blockquote>','') 
                line7=line6.replace('</blockquote>','')
                line8=line7.replace('<u>','')
                line9=line8.replace('</font>','')                  
                if "font color" in line9:
                    line9=line9.replace('<font color="#333333">','')
                    Ans=line9
                    ans = (str(counter)+" : "+Ans)
                    answerList.append(ans)
                    #continue    
                questionList.append(line9)                   
                #print(line)
    #answer="Answer: "+Ans
    #questionList.append(answer)
    leng = len(questionList)
    if "Explanation" in questionList[leng-1] :
        #questionList[leng-1],questionList[leng-2] = questionList[leng-2],questionList[leng-1]
        answerList.append(questionList[leng-1])
        del questionList[-1]
    questionList.append("--------------------------------------------------------------------------------------------------")
    with open(finalfile, 'a') as finalfile:
        for i in range(len(questionList)):
            print(questionList[i])
            finalfile.writelines(questionList[i])
            finalfile.write('\n')
    err_fname.close()
    
    answerList.append("--------------------------------------------------------------------------------------------------")
    with open(ansfile, 'a') as ansfile:
        for i in range(len(answerList)):
            print(answerList[i])
            ansfile.writelines(answerList[i])
            ansfile.write('\n')
    err_fname.close()

targetFileName='urllist_Final.txt'
targetFolder=os.getcwd()
if os.path.exists(os.path.join( targetFolder,'data')):
    csvfilex = os.path.join( targetFolder,'data',targetFileName)
else:
    os.makedirs(os.path.join( targetFolder,'data'))
    csvfilex = os.path.join( targetFolder,'data',targetFileName)

with open(csvfilex, 'r') as err_fname:
        for line in err_fname:
            counter+=1
            #print(line)
            URLExtract(line,counter)
  

# for url in urllist:
#     counter+=1
#     URLExtract(url,counter)
    