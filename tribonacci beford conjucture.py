import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def diff(a,b):
    for i in range (2,len(b)):
        dif=b[i]-b[i-1]
        a.append(dif)
    return a     

def seedval(x,y):
    a1=a2=a3=a4=a5=a6=a7=a8=a9=0
    for a in y:
        if a[0] == '1':
            a1+=1
        if a[0] == '2':
            a2+=1
        if a[0] == '3':
            a3+=1
        if a[0] == '4':
            a4+=1
        if a[0] == '5':
            a5+=1
        if a[0] == '6':
            a6+=1
        if a[0] == '7':
            a7+=1
        if a[0] == '8':
            a8+=1
        if a[0] == '9':
            a9+=1
            
    x.extend([a1,a2,a3,a4,a5,a6,a7,a8,a9])
    return x

def percval(p,ls):
    for i in p:
        perc = (i/n)*100
        ls.append(perc)
    return ls


#Main tribonacci series
a,b,c=0,1,1
elem =[a,b,c]
n = int(input("Enter no of terms: "))
for i in range(n):
    d=a+b+c
    a,b,c = b,c,d
    elem.append(str(d))
    
intelem=[int(i) for i in elem]
# print(intelem)

#Sucessive difference of element in list
lsd=[]
lsd2=[]
lsd3=[]
lsd = diff(lsd,intelem)
lsd2 = diff(lsd2,lsd)
lsd3 = diff(lsd3,lsd2)
# print(lsd, lsd2, lsd3, sep="\n")

#Converting all integer elements in list into string to extract seed values
strlsd2= [str(i) for i in lsd2]
strlsd1= [str(i) for i in lsd]
strlsd0= [str(i) for i in intelem]

#Obtaining seed values
nlsd0=[]
nlsd1=[]
nlsd2=[]
seedval(nlsd0,strlsd0)
seedval(nlsd1,strlsd1)
seedval(nlsd2,strlsd2)

#Calculating the contribution to total of each seed values
ls1=[]
ls2=[]
ls3=[]
percval(nlsd0,ls1)
percval(nlsd1,ls2)
percval(nlsd2,ls3)

#Subpolot grid
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 8))

plt.subplot(121) #Subplot-1

#Bar graph plotting
X=['1','2','3','4','5','6','7','8','9']
yelem = ls1
ylsd = ls2
ylsd2=ls3
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2 , yelem, 0.2)
plt.bar(X_axis , ylsd, 0.2)
plt.bar(X_axis + 0.2, ylsd2, 0.2)


 
plt.xticks(X_axis,X)
plt.xlabel("Seed values")
plt.ylabel("Percentage of seed value")
plt.title("Benford's law and tribonacci for first "+ str(n) + " terms" ,fontsize = 18)
plt.legend(["Initial stage","First difference set","Second difference set"], fontsize=15)

plt.subplot(122)  #Subplot-2

#Distribution plot
seed = []
for i in strlsd0:
    seed.append(int(i[0]))



sns.distplot(seed)
plt.ylabel("Probability Distribution")
plt.xlabel("Seed values")
plt.title("Probability Distribution of initial seed values", fontsize=18)
plt.show()

#Save subplots
fig.savefig("output.jpg")

print("Your Plot is stored as 'output.jpg' in the parent directory")

