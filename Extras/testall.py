import os
d="./wv"
files=os.listdir(d)


for f in files:
	if(f[-3:]=="txt"):
		os.system("python eval-word-vectors-master/all_wordsim_mod.py wv/"+f+" eval-word-vectors-master/data/word-sim/ > ovwv/" + f[:-4]+"res.txt")