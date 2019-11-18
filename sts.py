#Evaluate for  Semantic Textual Similarity
from scipy.spatial import distance
import operator
import numpy as np

import csv
import numpy as np
from os import listdir
from os.path import isfile, join
import os


def sts_eval(data,vocab):
    v=0
    files = [f for f in listdir('STS')]
    files = sorted(files)
    for file in files:
        if(file[0:2]=='FY' ):
            f=open('STS/'+file,'r')
            f1=open('STS/O'+file[:-4]+'.txt','w')
            c=0
    #         print(file)
            reader=csv.reader(f,delimiter='\t')
            for row in reader:
                p="\t".join(row)
                row=p.split('\t')

                if(file[2]=='B'):
                    try:
                        s1,s2=row[5],row[6]
                    except:
                        print(file,row)
                else:
                    s1,s2=row[4],row[5]
                w1s=s1.split()
                w2s=s2.split()
            #     print(w1s)
                r=[str(w).lower() for w in w1s]
                r1=[data[re] for re in r if re in data]
                r=[str(w).lower() for w in w2s]
                r2=[data[re] for re in r if re in data]
                sim=0
                if len(r1)>0 and len(r2)>0:
                    rr1=np.vstack(r1)
                    rr2=np.vstack(r2)
                    rep1=rr1.sum(axis=0)
                    rep2=rr2.sum(axis=0)
                    sim=1-distance.cosine(rep1,rep2)
        #             print(c,len(rep1),len(rep2))
                c += 1
                f1.write(str(sim))
                f1.write("\n")
            f1.close()
            f.close()
            # print("Start"+file[-8:-4])
            # print(file)
            if(file[2]=='B'):
                cor_eval='ben.pl'
            else:
                cor_eval='com.pl'
            s=os.popen('perl STS/'+cor_eval+' STS/'+file+' STS/O'+file[:-4]+'.txt').read()
            print(file[-8:-4]+"_"+file[3:-8]+"_"+file[:3]," ",s[7:-1])
            # print("End"+file[-8:-4])
            # for i in range(10000):
            #     v+=1
            #     continue
            # print(file,cor_eval)


    # cs17mtech11004@digserver:~/code/Evaluation$ awk -F "\t" '{print $0 >> ("F" $1$2 "MT.csv")}' stscompanion/sts-mt.csv
# cs17mtech11004@digserver:~/code/Evaluation$ awk -F "\t" '{print $0 >> ("F" $1$2 "Other.csv")}' stscompanion/sts-other.csv
# 2012_MSRpar_FYB
# 2014_deft-forum_FYB
# 2015_answers-forums_FYB
# 2016_postediting_FYC
