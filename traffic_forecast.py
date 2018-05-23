"""
Problem ta hocche ami p array ta clf.fit e argument dite chai.p ta holo amar input array ar y ta output array.
Changes gulo kore diye amar whatsapp no. e diye dio program ta please.9647972747"""



import numpy as np
from sklearn import linear_model
array=[]
x=[]
k=[]
g=[]
b=[]
y=[]
p=[]
n=input()
j=0
array=np.array([raw_input().split() for _ in range(n)],str)
for i in range (n):
    x.append(array[i][0])
    y.append(array[i][1])
for i in range (n):
    p.append(int(filter(str.isdigit,x[i])))#Extract numbers from string.
for i in range (n):
    k.append(p[i])
#To make the array 2 by n
#b=np.linalg.pinv(g.T)
#c=np.matmul(b,y)
y = [int(numeric_string) for numeric_string in y]
g=np.vstack((k,p,y))#To insert 2 1d arrays in a 2d array
b=g.T

c=[]
c1=[]
np.reshape(p,(1,-1))
p=np.array(p)
for i in range (12):
    c.append(1)    
for i in range(12):
    c1.append(n+i+1)
c2=[]
c3=[]
c2=np.vstack((c1,c1))
c3=c2.T
clf = linear_model.Lasso(alpha=0.1)#Experiment with n_estimator value.Here its optimal value is 75
clf.fit(b[:,:-1],b[:,-1])
prediction=clf.predict(c3)

for i in prediction:
    print(i)
#print(clf.predict(c2.T))
#plt.scatter(p, y, c="r", alpha=1)
#plt.show()
