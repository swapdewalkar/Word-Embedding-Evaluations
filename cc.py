from scipy.spatial import distance
import operator
import numpy as np
from sklearn.cluster import KMeans

def calculate_purity(dataset,N,data,vocab):
    y_pred = KMeans(n_clusters=N,init='k-means++').fit_predict(data)
    f=open('word-benchmarks-master/word-categorization/monolingual/en/'+dataset+'.csv')
    data=f.read().split("\n")
    concept=set()
    cat=set()
    AP_cluster={}
    AP_cluster_found={}
    for r in data:
        a = r.split(",")
        if(len(a)>=3) and a[0]!='' and a[2]!='':
            concept.add(a[2])
            cat.add(a[1])
            if a[2] in vocab:
                if a[1] in AP_cluster_found:
                    AP_cluster_found[a[1]].append(a[2])
                else:
                    AP_cluster_found[a[1]]=[a[2]]
            if a[1] in AP_cluster:
                AP_cluster[a[1]].append(a[2])
            else:
                AP_cluster[a[1]]=[a[2]]
#     print(len(concept),len(cat))
#     vocab_found=[]
#     vocab_not_found=[]
#     for c in concept:
#         if c in vocab:
#             vocab_found.append(c)
#         else:
#             vocab_not_found.append(c)
#     for k in AP_cluster:
#         print(k,len(AP_cluster[k]))
#     for k in AP_cluster_found:
#         print(k,len(AP_cluster_found[k]))

    predicated_cluster={}
    for p in range(len(y_pred)):
#         print(p,vocab[p])
        if y_pred[p] not in predicated_cluster:
            predicated_cluster[y_pred[p]]=[vocab[p]]
        else:
            predicated_cluster[y_pred[p]].append(vocab[p])
#     for k in predicated_cluster:
#         print(k,len(predicated_cluster[k]))
    matrix={}
    for c in AP_cluster_found:
        matrix[c]=np.zeros(21) 
        for con in AP_cluster_found[c]:
            for k in predicated_cluster:
                if con in predicated_cluster[k]:
                    matrix[c][k]+=1
    s=0
    sm=0
    for c in matrix:
        sm+=matrix[c].sum()
        s+=max(matrix[c])

    print(dataset,':',s/sm)

def cc_eval(data,vocab):
    calculate_purity('ap',21,data,vocab)
    calculate_purity('essli-2008',6,data,vocab)
    calculate_purity('battig',10,data,vocab)