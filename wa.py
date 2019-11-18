#//Testing Word Analogy

from scipy.spatial import distance
import operator
import numpy as np
import sys

def wa_eval(data,vocab):

    #Read Word Analogy
    f=open('questions-words.txt')
    queword=f.read()
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

    #Check for every type 
    for k in D:
        correct=0
        total=0
        similar={}
        for p in D[k]:
            a,b,c,d=p
            if a in data and b in data and c in data and d in data:
    #             print(a,b,c,d)
                total+=1
                w=data[b]-data[a]+data[c]
                v=data[d]
                for i in data:
                    similar[i]=distance.cosine(w,data[i])
                  # similar[i]=distance.euclidean(w,data[i])
                sim=sorted(similar.items(), key=operator.itemgetter(1))
                i=0
                for a,b in sim:
                    if i<5:
                        if a==d:
                            correct+=1
                            break
                        i+=1
        if total!=0: 
            print(k,":",correct*100/total,':',"Total-",len(D[k]),"Found-",total,"Correct-",correct)
        else:
            print(k,":",0,':',"Total-",len(D[k]),"Found-",total,"Correct-",correct)  

# gram8-plural : Total- 1332 Found- 342 Correct- 127 Accuracy- 37.134502923976605
# capital-world : Total- 4524 Found- 0 Correct- 0
# gram1-adjective-to-adverb : Total- 992 Found- 756 Correct- 64 Accuracy- 8.465608465608465
# gram2-opposite : Total- 812 Found- 156 Correct- 1 Accuracy- 0.6410256410256411
# gram7-past-tense : Total- 1560 Found- 756 Correct- 321 Accuracy- 42.46031746031746
# gram4-superlative : Total- 1122 Found- 462 Correct- 0 Accuracy- 0.0
# city-in-state : Total- 2467 Found- 0 Correct- 0
# family : Total- 506 Found- 132 Correct- 0 Accuracy- 0.0
# gram3-comparative : Total- 1332 Found- 1260 Correct- 91 Accuracy- 7.222222222222222
# capital-common-countries : Total- 506 Found- 0 Correct- 0
# gram6-nationality-adjective : Total- 1599 Found- 0 Correct- 0
# gram5-present-participle : Total- 1056 Found- 552 Correct- 193 Accuracy- 34.96376811594203
# gram9-plural-verbs : Total- 870 Found- 506 Correct- 148 Accuracy- 29.24901185770751
# currency : Total- 866 Found- 0 Correct- 0