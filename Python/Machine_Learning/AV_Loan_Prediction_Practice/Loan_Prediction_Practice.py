import pandas as pd
import numpy as np
from scipy.stats import mode
import matplotlib.pyplot as plt
from boto.mws.connection import dependent
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing,cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, LinearSVC

# get train & test csv files as a DataFrame
df_train = pd.read_csv('train_u6lujuX_CVtuZ9i.csv')
df_test = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')


# Dropping Loan Id as it's not useful in analysis and prediction
df_train.drop(['Loan_ID'],axis=1,inplace=True)

# The Gender column has some missing values so we'll update the missing records with unknown
df_train["Gender"] = df_train["Gender"].fillna("Male")
df_test["Gender"] = df_train["Gender"].fillna("Male")

def get_gender(gender):
    gen=0
    if gender =='Male':
        gen=0
    elif gender =='Female':
        gen=1
    else:
        gen=2
    return gen
    

df_train['Gender'] = df_train['Gender'].apply(get_gender)
df_test['Gender'] = df_test['Gender'].apply(get_gender)

# Three records has missing married column so updating them with Yes which is the mode
df_train["Married"] = df_train["Married"].fillna('Yes')
df_test["Married"] = df_test["Married"].fillna('Yes')

def get_married(status):
    return 0 if status =='Yes'  else 1

df_train['Married'] = df_train['Married'].apply(get_married)
df_test['Married'] = df_test['Married'].apply(get_married)

# Creating 2 categories for Dependents by replacing everything other than 0 as 1 as the ratios are similar
def get_dependents(dependents):
    return '0' if dependents =='0'  else '1'

df_train['Dependents'] = df_train['Dependents'].replace('3+',3)
df_test['Dependents'] = df_train['Dependents'].replace('3+',3)
df_train["Dependents"] = df_train["Dependents"].fillna(0)
df_test["Dependents"] = df_test["Dependents"].fillna(0)
#df_test['Dependents'] = df_test['Dependents'].apply(get_dependents)

def get_loan_status(status):
    return 0 if status =='N'  else 1

df_train['Loan_Status'] = df_train['Loan_Status'].apply(get_loan_status)

def get_education(status):
    return 0 if status =='Graduate'  else 1

df_train['Education'] = df_train['Education'].apply(get_education)
df_test['Education'] = df_test['Education'].apply(get_education) 
 
# Updating the missing Self Employed records with No which is the mode
def get_selfemp(status):
    return 0 if status =='No'  else 1

df_train["Self_Employed"] = df_train["Self_Employed"].fillna('No')
df_test["Self_Employed"] = df_test["Self_Employed"].fillna('No')

df_train['Self_Employed'] = df_train['Self_Employed'].apply(get_selfemp)
df_test['Self_Employed'] = df_test['Self_Employed'].apply(get_selfemp)


# Updating the missing Loan amount records with Median values
df_train["LoanAmount"].fillna(df_train["LoanAmount"].mean(), inplace=True)
df_test["LoanAmount"].fillna(df_test["LoanAmount"].mean(), inplace=True)

#  Update the Loan amount term with Mode
df_train["Loan_Amount_Term"].fillna(df_train["Loan_Amount_Term"].median(), inplace=True)
df_test["Loan_Amount_Term"].fillna(df_test["Loan_Amount_Term"].median(), inplace=True)

# Updating the credit history to '1' as the ratio to loan given/ rejected is nearer to 1 than 0

df_train["Credit_History"] = df_train["Credit_History"].fillna(1)
df_test["Credit_History"] = df_test["Credit_History"].fillna(1)

def get_location(location):
    loc=2
    if location =='Urban':
        loc=0
    elif location =='Rural':
        loc=1
    else:
        loc=2
    return loc
    

df_train['Property_Area'] = df_train['Property_Area'].apply(get_location)
df_test['Property_Area'] = df_test['Property_Area'].apply(get_location)

# Preview the data
#print(df_test.head())
#print(df_train.groupby(["Dependents",'Loan_Status']).size())
#print(df_train.groupby(['Self_Employed']).size())

df_train.info()
# df_test.info()

# Copied the Test file to retrieve the Loan ID's later
# df_orig = df_test.copy()
df_train.to_csv('before.csv')
# le = preprocessing.LabelEncoder()
# for i in range(12):
#     df_train.iloc[:,i] = le.fit_transform(df_train.iloc[:,i])
# 
# le1 = preprocessing.LabelEncoder()
# for j in range(11):
#     df_test.iloc[:,j] = le1.fit_transform(df_test.iloc[:,j])

# df_train.to_csv('After.csv')

X_train = df_train.drop("Loan_Status",axis=1)
Y_train = df_train["Loan_Status"]
X_test  = df_test.drop("Loan_ID",axis=1)
# 
# print(df_test)

# random_forest = RandomForestClassifier(n_estimators=100)
# random_forest.fit(X_train, Y_train)
# Y_pred = random_forest.predict(X_test)
# random_forest.score(X_train, Y_train)

# logreg = LogisticRegression()
# logreg.fit(X_train, Y_train)
# Y_pred = logreg.predict(X_test)
# logreg.score(X_train, Y_train)

svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
svc.score(X_train, Y_train)

# X_Train,X_Test,y_Train,y_Test= cross_validation.train_test_split(X_t,y_t,test_size=0.2)
# 
# random_forest = RandomForestClassifier(n_estimators=5)
# 
# random_forest.fit(X_Train, y_Train)
# 
# accuracy = random_forest.score(X_Train, y_Train)
# Y_pred = random_forest.predict(X_test)


submission = pd.DataFrame({
        "Loan_ID": df_test["Loan_ID"],
        "Loan_Status": Y_pred
    })
submission.to_csv('Submission.csv', index=False)


df_n = pd.read_csv('Submission.csv')

df_n["Loan_Status"].replace('0','N',inplace=True)
df_n["Loan_Status"].replace(1,'Y',inplace=True)

df_n.to_csv('Submission_final.csv',index=False)


