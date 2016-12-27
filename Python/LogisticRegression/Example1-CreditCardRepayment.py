import numpy as np
import matplotlib as plt
from sklearn.linear_model import LogisticRegression

x = np.array([[10000,80000,35],[7000,120000,57],[100,23000,22],[223,18000,26]])
y = np.array([1,1,0,0])

classifier = LogisticRegression()
classifier.fit(x,y)

print(classifier.predict([5500,50000,25]))