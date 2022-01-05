
import requests
from parsel import Selector
from array import*
arr1=[]
arr2=[]
ww=[]
a=[]
arr=[]
R1=[]
R2=[]
r= requests.get('https://zeenews.india.com/india')
text=r.text
#print(text)

s= Selector(r.text)
href_links = [s.xpath('//img/@title').getall()]
l2=len(href_links[0])
#print(l2)
k2=0
t2=0
g=""
k3=""
k4=0
t1=0
t=0
for y in range(0,l2):
    l1=len(href_links[0][y])
    #print(l1)
    #print(href_links[0][y])
    for i in range(0,l1):
        if href_links[0][y][i]==" ":
            k4=k4+1
    t=0
    
    for i in range(0,l1):
        r=t
        g=""
        if href_links[0][y][i]==" ":
            k2=k2+1
            t=i
            k3=""
            for j in range(r,i):
                k3=k3+href_links[0][y][j]
                if( k3=="Attack" or k3=="Collapsed" or k3=="collapsed"or k3=="pulwama" or k3=="collapses" or k3=="collase" or k3=="Collapsed" or k3=="dead" or k3=="death" or k3=="attacks" or k3=="injured" or k3=="Pulwama" or k3=="attack"):
                
                    g=y
                    ww.append(y)
                t1=j+2
                
            t=t+1
        
            k3=""
            if k2==k4:
                for k in range(t1,l1):
                    k3=k3+href_links[0][y][k]
            

            if(k3=="Attack" or k3=="Collapsed" or k3=="collapsed" or k3=="pulwama" or k3=="collapses" or k3=="Collapsed" or k3=="collase" or k3=="dead" or k3=="death" or k3=="attacks" or k3=="injured" or k3=="Pulwama" or k3=="attack"):
                g=y
                ww.append(y)


print("REQUIRED OUTPUT")
llist=len(ww)    
print(ww)
for i in ww:
    print(href_links[0][i])
print("\n")
print("NEXT NEWS")


ww1=[]
a1=[]
r1= requests.get('https://timesofindia.indiatimes.com/india')
text1=r1.text
#print(text1)

s= Selector(r1.text)
href_links1 = [s.xpath('//a/@title').getall()]
l21=len(href_links1[0])
#print(l21)
k21=0
t21=0
g1=""
k31=""
k41=0
t11=0
tt=0
for y in range(0,l21):
    l11=len(href_links1[0][y])
    #print(l1)
    #print(href_links1[0][y])
    for i in range(0,l11):
        if href_links1[0][y][i]==" ":
            k41=k41+1
    tt=0
    
    for i in range(0,l11):
        r=tt
        g=""
        if href_links1[0][y][i]==" ":
            k21=k21+1
            tt=i
            k31=""
            for j in range(r,i):
                k31=k31+href_links1[0][y][j]
                if( k31=="Attack" or k31=="Collapsed" or k31=="collapsed" or k31=="pulwama" or k31=="collapses" or k31=="collase" or k31=="Collapsed" or k31=="dead" or k31=="death" or k31=="attack" or k31=="attacks" or k31=="injured" or k31=="Pulwama"):
                
                    g1=y
                    ww1.append(y)
                t11=j+2
                
            tt=tt+1
        
            k31=""
            if k21==k41:
                for k in range(t11,l11):
                    k31=k31+href_links1[0][y][k]
            
            if( k31=="Attack" or k31=="Collapsed" or k31=="collapsed" or k31=="pulwama" or k31=="collapses" or k31=="collase" or k31=="Collapsed" or k31=="dead" or k31=="death" or k31=="attack" or k31=="attacks" or k31=="injured" or k31=="Pulwama"):
                
            
                g1=y
                ww1.append(y)


print("REQUIRED OUTPUT")
llist1=len(ww1)
print(ww1)
for i in ww1:
    print(href_links1[0][i])


k2=0
t2=0
g=""
k3=""
k4=0
t1=0
t=0
b=len(ww)
q=len(ww1)
k21=0
t21=0
g1=""
k31=""
k41=0
t11=0
tt=0
c=0
r=0
r1=0
for y in ww:
    b1=len(href_links[0][y])
    for i in range(0,b1):
        if href_links[0][y][i]==" ":
            k4=k4+1
            
    for i in range(0,b1):
        
        if href_links[0][y][i]==" ":
            k2=k2+1
            t=i
            k3=0
            if r==0:
                k3=str(k3)+(href_links[0][y][r])
            for j in range(r+1,i):
                k3=str(k3)+(href_links[0][y][j])
                t1=j+2
            x=k3
            arr1.append(x)
            #print(x)
            r=t
            k3=0
            if k2==k4:
                for k in range(t1,b1):
                    k3=str(k3)+(href_links[0][y][k])
                x=k3
                arr1.append(x)
                #print(x)
                r=0
        
    #print(arr1)
    arr=arr1.copy()
    R1.append(arr)
    arr1.clear()
print(R1)
          
for y1 in ww1:
    q1=len(href_links1[0][y1])
    for i in range(0,q1):
        if href_links1[0][y1][i]==" ":
            k41=k41+1
            
    for i in range(0,q1):
        if href_links1[0][y1][i]==" ":
            k21=k21+1
            tt=i
            k31=0
            if r1==0:
                k31=str(k31)+(href_links1[0][y1][r1])
            for j in range(r1+1,i):
                k31=str(k31)+(href_links1[0][y1][j])
                t1=j+2
            y=k31
            arr2.append(y)
            #print(y)
            r1=tt
            k31=0
            if k21==k41:
                for k in range(t1,q1):
                    k31=str(k31)+(href_links1[0][y1][k])
                y=k31
                arr2.append(y)
                #print(y)
                r1=0
    #print(arr2)
    ar=arr2.copy()
    R2.append(ar)
    arr2.clear()
print(R2)          #now we are having two list now compare those two

c=[]
count=0
for i in range(0,len(R1)):
    
    a=len(R1[i])
    for i1 in range(0,a):
        for j in range(0,len(R2)):
            b=len(R2[j])
            for j1 in range(0,b):
                if R1[i][i1]==R2[j][j1]:
                    print("comon  =",R1[i][i1])
                    count=count+1
                    
    print(" total count =",count)
    c.append(count)
    count=0
print("array for all counts  =",c)
lar=max(c)
z=(ww[c.index(lar)])
print("TODAY'S TOP NEWS ::",href_links[0][z])







