import re
import os
from statistics import stdev

dir = "C:\\Users\\wohangye\\Desktop\\twonorm"
filename = "bupa"
filenum = 1

train = 0
test = 0
rule = 0
time = 0
temp_cnt = 1
temp_train = 0
temp_test = 0
file_count = 1
TencvTime = 0
count = 0
testVa = []
trainVa = []

os.chdir(dir)
for path, subdirs, files in os.walk("."):
    for f in files:
        f = os.path.join(path, f)
        if f.endswith(".txt") and f.find("result"):
            if f.find("result10") is -1:
                f = open(f, "r")
                line=f.readline()
                while line:
                    if line.find("training accuracy")== 0:
                        print(count)
                        print(f)

                        count += 1
                        Str=line.split("=")
                        train+=float(Str[1])
                        temp_train += float(Str[1])
                        trainVa.append(float(Str[1]))
                    elif line.find("test accuracy")== 0:
                        Str=line.split("=")
                        print (float(Str[1]))
                        test+=float(Str[1])
                        temp_test += float(Str[1])
                        testVa.append(float(Str[1]))
                    elif re.search("Default rule",line):
                        Str=line.split(":")
                        rule+=float(Str[0])+1
                    elif line.find("Total time")==0:
                        Str=line.split(":")

                    line=f.readline()

                f.close()
                file_count += 1

print (count)
outfile=open("result.txt","w")
outfile.write("%f %f %f %f %f %f\n"%(rule/count, 100 - 100*train/count
                               ,100 - 100*test/count,time/(10*filenum), stdev(trainVa), stdev(testVa)))

outfile.close()
