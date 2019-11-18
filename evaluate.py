import sys
import os
from wa import wa_eval
from sts import sts_eval
from cc import cc_eval
import datetime

# python evaluate.py ~/openke/Code/OpenKE/res/Reviews_All_Output/entities_vecReviews_All_Rels.txt
# python evaluate py filename
# from ws import ws_eval 
from Eval_Word_Sim.ws_inside import ws_eval
import numpy as np
#Get vector file name
name=sys.argv[1]
out=sys.argv[2]
filename=name.split('/')[-1]
sys.stdout = open('Eval_Result/OUT_'+out+'_'+filename, 'w')

#Set all vector in vocabulary
def getVector(file):
    data={}
    vocab=[]
    vecs=[]
    data1=open(file).read().split("\n")[1:]
    for i in range(len(data1)):
        d1=data1[i].split(" ")
        word1=d1[0]
        vec=np.array(d1[1:-1],dtype=float)
        if(len(word1)>0):
            data[word1]=vec;
            vocab.append(word1)
            vecs+=[vec]
    P=np.vstack(vecs)
    return data,vocab,P

data,vocab,P=getVector(name)
print("STS")
sts_eval(data,vocab)
print("WS")
ws_eval('eval-word-vectors-master/data/word-sim/', name)
print("Concept Categarization")
cc_eval(P,vocab)
# print("WA")
# wa_eval(data,vocab)
#os.system("python eval-word-vectors-master/all_wordsim_mod.py "+name+" eval-word-vectors-master/data/word-sim/ ")
