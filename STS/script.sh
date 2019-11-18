rm -f *.csv
rm -f *.txt
cp Main/SICK_Original.csv FYCSICK.csv
#B- Benchmark
#C- Companion
#awk -F "\t" '{print $0 >> ("FMC" $1$2 ".csv")}' Main/sts-other.csv
#awk -F "\t" '{print $0 >> ("FOC" $1$2 ".csv")}' Main/sts-mt.csv
#awk -F "\t" '{print $0 >> ("FRB" $2$3 ".csv")}' Main/sts-train.csv
#awk -F "\t" '{print $0 >> ("FDB" $2$3 ".csv")}' Main/sts-dev.csv
#awk -F "\t" '{print $0 >> ("FSB" $2$3 ".csv")}' Main/sts-test.csv
#awk -F "\t" '{print $0 >> ("FBB" $2$3 ".csv")}' Main/sts-train.csv
#awk -F "\t" '{print $0 >> ("FBB" $2$3 ".csv")}' Main/sts-dev.csv
#awk -F "\t" '{print $0 >> ("FBB" $2$3 ".csv")}' Main/sts-test.csv

awk -F "\t" '{print $0 >> ("FYC" $1 substr($2,1,4) ".csv")}' Main/sts-other.csv
awk -F "\t" '{print $0 >> ("FYC" $1 substr($2,1,4) ".csv")}' Main/sts-mt.csv
awk -F "\t" '{print $0 >> ("FYB" $2 substr($3,1,4) ".csv")}' Main/sts-train.csv
awk -F "\t" '{print $0 >> ("FYB" $2 substr($3,1,4) ".csv")}' Main/sts-dev.csv
awk -F "\t" '{print $0 >> ("FYB" $2 substr($3,1,4) ".csv")}' Main/sts-test.csv
