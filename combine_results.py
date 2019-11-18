import sys
import os
files=os.listdir("TEMP_Result")
D={}
sts={}
ws={}
cc={}
wa={}
def create_dict_from_array(arr,T):
    d={}
    t={}
    c={}
    f={}
    flag=0
    for a in arr:
        # if flag==0:
        #     flag=1
        #     continue

        print(a)
        k,v=a.split(":")[:2]
        k=k.strip()
        v=float(v.strip())
        # print(k,v)
        d[k]=""
        d[k]=v
        # print(d)
        if T=='STS':
            sts[k]=""
        elif T=='WS':
            ws[k]=""
        elif T=='WA':
            count=a.split(":")[2].strip()
            p,q,r,s=count.split("- ")
            total=int(q.split()[0])
            found=int(r.split()[0])
            correct=int(s)
            print(total,found,correct)
            wa[k]=""
            t[k]=total
            f[k]=found
            c[k]=correct
        else:
            cc[k]=""

    if T=='WA':
        return d,t,c,f 
    return d

for file in files:
    D[file]={}
    # print(file)
    f=open("TEMP_Result/"+file)
    data=f.read().split("\n")
    STS = data[1:27]
    WS  = data[28:41]
    CC  = data[42:45]
    WA  = data[46:60]
    # print(STS,WA,WS,CC)
    D[file]['STS']=create_dict_from_array(STS,"STS")
    D[file]['WS']=create_dict_from_array(WS,"WS")
    D[file]['CC']=create_dict_from_array(CC,"CC")
    D[file]['WA'],D[file]['T'],D[file]['F'],D[file]['C']=create_dict_from_array(WA,"WA") 
print(D)
 
    
