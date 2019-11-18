from scipy.spatial import distance
import operator
import numpy as np
import sys
# import sklearn.metrics.pairwise_distances
def load_to_file(name,folder):
    with open(folder+"/"+name,'rb') as f:
        ret=pickle.load(f)
        f.close()
        return ret

def Simillar(h_vectors,r_vectors,t_vectors,word,k,cos,rels):
    global c
    row=word+"\t"
    h=h_vectors[word]
    print(c)
    c += 1
    for relation in rels:
        r=r_vectors[relation]
        h_r=h+r
        # print(word,relation)
        sim={}
        for i in t_vectors:
            if cos==True:
                sim[i]=distance.cosine(h_r,t_vectors[i])
            else:
                sim[i]=distance.euclidean(h_r,t_vectors[i])
        sim=sorted(sim.items(), key=operator.itemgetter(1))
        i=0
        for a,b in sim:
            i+=1
            if i==1:
                continue
            row+=a+"\t"
            if i>k:
                break
    return row
output_folder=sys.argv[1]
name=sys.argv[2]
no_of_words=int(sys.argv[3])
output_file=sys.argv[4]

h_file = output_folder+'/entities_vec'+name+'.txt' 
r_file = output_folder+'/relations_vec'+name+'.txt'
t_file = output_folder+'/entities_vec'+name+'.txt'

# Simillar(h_file,r_file,t_file,'phone',5,False)

c=0
h_vectors=[]
h_list=[]
r_vectors=[]
r_list=[]
t_vectors=[]
t_list=[]
h_data=open(h_file).read().split("\n")
for i in range(len(h_data)):
    d1=h_data[i].split(" ")
    word1=d1[0]
    vec=np.array(d1[1:-1],dtype=float)
    if(len(word1)>0):
        # h_vectors[word1]=vec;
        h_vectors.append(vec)
        h_list.append(word1)

r_data=open(r_file).read().split("\n")
for i in range(len(r_data)):
    d1=r_data[i].split(" ")
    word1=d1[0]
    vec=np.array(d1[1:-1],dtype=float)
    if(len(word1)>0):
        r_vectors.append(vec)
        r_list.append(word1)

t_data=open(t_file).read().split("\n")
for i in range(len(t_data)):
    d1=t_data[i].split(" ")
    word1=d1[0]
    vec=np.array(d1[1:-1],dtype=float)
    if(len(word1)>0):
        t_vectors.append(vec)
        t_list.append(word1)
print(len(h_list),len(r_list),len(t_list))
data=""
# rels=['synset','hypernym','hyponym','weak','holonym','strong','antonym']
# data="Word"+"\t"
# for rel in rels:
#     for n in range(no_of_words):
#         data+=rel.capitalize()+" "+str(n+1)+"\t"
# data+="\n"

# for i in heads:
#     data+=Simillar(h_vectors,r_vectors,t_vectors,i,no_of_words,False,rels)+"\n"

# print(h_vectors[0][:10])
# print(r_vectors[0][:10])
# print(h_r_vectors[0][:10])
# print(r_list)
from datetime import datetime
rs=[ 'antonym', 'synset', 'hyponym', 'hypernym', 'holonym', 'strong', 'weak']
print(str(datetime.now()))
for i in range(len(r_list)):
    if r_list[i] in rs:
        h_r_vectors=np.array((np.array(h_vectors)-np.array(r_vectors[i])))
        sim=distance.cdist(h_r_vectors,t_vectors)
        for j in range(len(sim)):
            # print(i,j)
            idx=np.argsort(sim[j])[1:no_of_words]
            res=np.take(t_list,idx)
            # print(res)
            data+=h_list[j]+"\t"+r_list[i]+"\t"+str('\t'.join(res))+"\n"
        print(str(datetime.now()))
print(str(datetime.now()))
with open(output_folder.split("/")[-1]+output_file+'.csv','w') as f:
    f.write(data)
    f.close()
# heads=sorted(heads)
# tails=sorted(tails)

# H_T={}
# for i in heads:
#     print(i)
#     for j in tails:
#         H_T[(i,j)]=h_vectors[i]-t_vectors[j]
#         pass

# print(H_T)