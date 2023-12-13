import inline
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import math
%reload_ext autoreload
%autoreload 2
X=100*np.random.rand(1000)
Y=100*np.random.rand(1000)
Z=np.array([[]])
for i in range (1000):
    Z=np.append(Z,[X[i],Y[i]])
Z=Z.reshape(1000,2)
print(Z[10])
plt.plot(X,Y,'.',color='blue')
r=1
for i in range(1000):
    Target=Z[i]
    Xt=math.floor(Target[0])
    Yt=math.floor(Target[1])
    Xmin=Xt-1
    Xmax=Xt
    Ymin=Yt-1
    Ymax=Yt
    if(Target[0]-Xt>0):
        Xmax=Xt+1
    if(Target[1]-Yt>0):
        Ymax=Yt+1
    for j in range(i+1,1000):
        P=math.floor(Z[j][0])
        Q=math.floor(Z[j][1])
        k=0
        if(Ymin<=Q and Q<=Ymax):
            k=k+1
        if(Xmin<=P and P<=Xmax):
            k=k+1
        if(k==2):
            plt.plot(Z[j][0],Z[j][1],'x',color='red')
            #Destination point is marked with red
            plt.plot(Z[i][0],Z[i][1],'x',color='green')
            #Target point is marked with green
#Now we generalize the code for different values of r. Keep in mind, that the region we have to consider for higher values of r won't always be a rectangle.
#But the required region will always lie in a rectangle of side p*q where p and q can be either 2r or 2r+1 (depending upon location of target point)

plt.plot(X,Y,'.',color='blue')
A=np.array([[[]]])
t=0
R=np.array([1,2,3,4,5,6,7,8,9,10])
r=R[2]
for i in range(1000):
     Target=Z[i]
     Xt=math.floor(Target[0])
     Yt=math.floor(Target[1])
     Xmin=Xt-r
     Xmax=Xt+r-1
     Ymin=Yt-r
     Ymax=Yt+r-1
     if(Target[0]-Xt>0):
         Xmax=Xt+1
     if(Target[1]-Yt>0):
         Ymax=Yt+1
     for j in range(i+1,1000):
         P=math.floor(Z[j][0])
         Q=math.floor(Z[j][1])
         k=0
         if(Ymin<=Q and Q<=Ymax):
             k=k+1
         if(Xmin<=P and P<=Xmax):
             k=k+1
         if(k==2):
             t=t+1
             A=np.append(A,[Z[i],Z[j]])
             plt.plot(Z[j][0],Z[j][1],'x',color='red')
             plt.plot(Z[i][0],Z[i][1],'x',color='green')
A=A.reshape(t,2,2)
print(A)
#Now we will extend to 3D and try plotting it
I=100*np.random.rand(1000)
J=100*np.random.rand(1000)
K=100*np.random.rand(1000)
Z=np.array([[]])
for i in range (1000):
    Z=np.append(Z,[I[i],J[i],K[i]])
Z=Z.reshape(1000,3)
print(Z[10])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(I,J,K,'.',color='blue')
A=np.array([[[]]])
t=0
R=np.array([1,2,3,4,5,6,7,8,9,10])
r=R[6]
for i in range(1000):
     Target=Z[i]
     It=math.floor(Target[0])
     Jt=math.floor(Target[1])
     Kt=math.floor(Target[2])
     Imin=It-r
     Imax=It+r-1
     Jmin=Jt-r
     Jmax=Jt+r-1
     Kmin=Kt-r
     Kmax=Kt+r-1
     if(Target[0]-It>0):
         Imax=It+1
     if(Target[1]-Jt>0):
         Jmax=Jt+1
     if(Target[2]-Kt>0):
         Kmax=Kt+1
     for j in range(i+1,1000):
         P=math.floor(Z[j][0])
         Q=math.floor(Z[j][1])
         R=math.floor(Z[j][2])
         k=0
         if(Jmin<=Q and Q<=Jmax):
             k=k+1
         if(Imin<=P and P<=Imax):
             k=k+1
         if(Kmin<=R and R<=Kmax):
             k=k+1
         if(k==3):
             t=t+1
             A=np.append(A,[Z[i],Z[j]])
             ax.plot3D(Z[j][0],Z[j][1],Z[j][2],'.',color='red')
             ax.plot3D(Z[i][0],Z[i][1],Z[i][2],'.',color='green')
A=A.reshape(t,2,3)
print(A)
#General Case of d, without plotting
N=np.array([[]])
D=np.array([4,5,10,50,100])
d=D[1]
for i in range (d):
    N=np.append(N,100*np.random.rand(1000))
N=N.reshape(d,1000)
Z=np.array([[]])
for i in range (1000):
    for j in range (d):
        Z=np.append(Z,[N[j][i]])
Z=Z.reshape(1000,d)
A=np.array([[[]]])
t=0
R=np.array([1,2,3,4,5,6,7,8,9,10])
r=R[6]
for i in range(1000):
     Target=Z[i]
     Tv=np.array([])
     for j in range (d):
         Tv=np.append(Tv,math.floor(Target[j]))
     Tmin=np.array([])
     for j in range (d):
         Tmin=np.append(Tmin,Tv[j]-r)
     Tmax=np.array([])
     for j in range (d):
         Tmax=np.append(Tmax,Tv[j]+r-1)
         if(Target[j]-Tmax[j]>0):
             Tmax[j]=Tmax[j]+1
     for j in range(i+1,1000):
         Dv=np.array([])
         for k in range (d):
             Dv=np.append(Dv,math.floor(Z[j][k]))
         q=0
         for k in range (d):
             if(Tmin[k]<=Dv[k] and Dv[k]<=Tmax[k]) :
                 q=q+1
         if(q==d):
             t=t+1
             A=np.append(A,[Z[i],Z[j]])
A=A.reshape(t,2,d)
print(A)