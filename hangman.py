import pandas as pd
import numpy as np

data=pd.read_csv("indian movies.csv")
data.drop(['ID','Timing(min)','Rating(10)','Votes','Genre'],axis=1,inplace=True)
data=data[data['Language']=='telugu']
data=data['Movie Name'].to_list()

#print(data[:10])
data.sort()
data=list(set(data))

from collections import Counter
def freq(list1,true_ltrs,false_ltrs,length):
    letters = "".join(list1)
    letter_count = Counter(letters)
    m=len(set("".join(list1)))
    highest_letter = letter_count.most_common(m)
    for i in range(m):
        if highest_letter[i][0] not in true_ltrs and highest_letter[i][0] not in false_ltrs:
            return highest_letter[i][0]

def intial_data(names,le):
    d=[i for i in names if len(i) == le]
    return d


def len_letters(names,max_l,ltr):
    d=[i for i in names if i.count(ltr)== max_l]
    return d

def index_data(names,index_pos,index_ltr):
    k=[i for i in names if i[index_pos] == index_ltr]
    return k

def remove(names,false_ltrs):
    k=[]
    for i in names:
        cnt=0
        for j in false_ltrs:
            if i.count(j) !=0 :
                cnt+=1
        if(cnt==0):
            k.append(i)
    return k
        

for i in range(len(data)):
    data[i]=data[i].replace(" ","")
    data[i]=data[i].replace(",","")
    data[i]=data[i].replace("-","")
    data[i]=data[i].replace(".","")
    data[i]=data[i].lower()

l=int(input("enter length of string : "))
op=['_' for i in range(l)]
op_len=0
true_ltrs=""
false_ltrs=""
d=intial_data(data,l)
iterations=0
while op_len < l and iterations != 6 and len(d) != 1:
    letter =  freq(d,true_ltrs,false_ltrs,l)
    print("predicted letter : " + letter)
    k = int(input("enter 1 or 0 : "))
    if(k):
        true_ltrs=true_ltrs+letter
        flag=0
        itrs=0
        while(flag != -1):
            h=int(input("enter index of letter : "))
            if(h == -1):
                flag=-1
            else:
                op_len+=1
                op[h-1]=letter
                d=index_data(d,h-1,letter)
                itrs+=1
        d=len_letters(d,itrs,letter)
        
    else:
        false_ltrs=false_ltrs+letter
        iterations +=1   
        d=remove(d,false_ltrs)
if len(d) ==1 :
    print("your movie : ",d[0])
else:
    print("your movie : "+"".join(op))   