

import requests
from parsel import Selector


p=[]
r= requests.get('https://zeenews.india.com/india')
text=r.text
#print(text)

s= Selector(r.text)
href_links = [s.xpath('//img/@title').getall()]
l2=len(href_links[0])

r1= requests.get('https://timesofindia.indiatimes.com/india')
text1=r1.text
#print(text1)

s1= Selector(r1.text)
href_links1 = [s1.xpath('//a/@title').getall()]
l21=len(href_links1[0])

def reqlist(href_links,l2):
    
    global ww
   
    
    ww=[]
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
    print(ww)

    
    

def filter(ww,href_links,l2):
    global p
    p=[]
    x=[]
    for i in range(0,len(ww)-1):
        if ww[i]==ww[i+1]:
            x.append(i)
    print(x)
    for j in range(0,len(x)):
        ww.pop(x[j])
    print(ww)
    arr1=[]
    R1=[]
    k4=0
    k3=""
    k2=0
    r=0
    t=0
    
    for y in ww:
        b1=len(href_links[0][y])
        for i in range(0,b1):
            if href_links[0][y][i]==" ":
                k4=k4+1
            
        for i in range(0,b1):
        
            if href_links[0][y][i]==" ":
                k2=k2+1
                t=i
                k3=""
                if r==0:
                    k3=str(k3)+(href_links[0][y][r])
                for j in range(r+1,i):
                    k3=str(k3)+(href_links[0][y][j])
                    t1=j+2
                x=k3
                arr1.append(x)
                #print(x)
                r=t
                k3=""
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
    #print(R1)
    p=R1.copy()
    for i in ww:
        print(href_links[0][i])
    print("\n")




    
            
reqlist(href_links,l2)
F1=ww    
filter(F1,href_links,l2)
Z1=p
#print(Z1)
print("next  news")
reqlist(href_links1,l21)
F2=ww
filter(F2,href_links1,l21)
Z2=p
#print(Z2)


c=[]
count=0
d=[]
for i in range(0,len(Z1)):
    
    a=len(Z1[i])
    for j in range(0,len(Z2)):
            b=len(Z2[j])
            for i1 in range(0,a):
                for j1 in range(0,b):
                    if Z1[i][i1]==Z2[j][j1]:
                        print("common word  =",Z1[i][i1])
                        count=count+1
                        if Z1[i][i1]=="in" or Z1[i][i1]=="and" or Z1[i][i1]=="for" or Z1[i][i1]=="to" or Z1[i][i1]=="on":
                            count=count-1
                    
            print(" common words in each sentence =",count)
            c.append(count)
            count=0
    d1=c.copy()
    d.append(d1)
    c.clear()
print("array for all counts  =",d)#array for each sentence count i.e array1*array2 elements


####up to here we completed till finding how many words are same in each senctence




l=[]
for i in range(0,len(Z1)-1):
    v=max(d[i])
    l.append(v)

print(l)# largst count in each array 
u=l.index(max(l))
prob=d[u]
#print(prob)
b=prob.index(max(prob))
u1=d[u][b]   ###here we got news max matched i.e either in array1 uth index or array2 bth index(suspect or imagining)
#print(u1)    ###so this is the most matched sentence and count of common words





if u1>2:##condition (confirming not only suspect)
    print("more common words found in these news")
    print(Z1[u])
    print(Z2[b])
else:
    print("Oops! no top news today ")



