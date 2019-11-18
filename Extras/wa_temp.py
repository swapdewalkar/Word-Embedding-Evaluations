#//Testing Word Analogy

from scipy.spatial import distance
import operator
import numpy as np
import sys

from sklearn.metrics.pairwise import cosine_similarity
def wa_eval(data,vocab,P):

    #Read Word Analogy
    f=open('questions-words.txt')
    queword=f.read().lower()
    ques=queword.split("\n")
    D={}
    p=""
    for q in ques:
        a=q.split(" ")
        if(a[0]==':'):
            D[a[1]]=[]
            p=a[1]
        else:
            if(len(a)>=4):
                D[p].append(a)

    categories=D.keys()
    categories=sorted(categories)
    #Check for every type 
    for k in categories:
        correct=0
        total=0
        similar={}
        aas=[]
        bs=[]
        cs=[]
        ds=[]
        dvocab=[]
        for p in D[k]:
            a,b,c,d=p
            if a in data and b in data and c in data and d in data:
                total+=1
                aas.append(data[a])
                bs.append(data[b])
                cs.append(data[c])
                ds.append(data[d])
                dvocab.append(d)
        dvocab=np.array(dvocab)
        if len(aas)!=0:
            aas  = np.vstack(aas)
            bs   = np.vstack(bs)
            cs   = np.vstack(cs)
            temps=bs-aas+cs
            sim=cosine_similarity(temps,P)
            sim_sorted_index=np.argsort(sim,axis=1)
            s=sim_sorted_index[:,-5:]
            sim_words=np.array(vocab)[s]
            for i in range(len(dvocab)):
                if dvocab[i] in sim_words[i]:
                    correct+=1    
        if total!=0: 
            print(k,":",correct*100/total,':',"Total-",len(D[k]),"Found-",total,"Correct-",correct)
        else:
            print(k,":",0,':',"Total-",len(D[k]),"Found-",total,"Correct-",correct)  

