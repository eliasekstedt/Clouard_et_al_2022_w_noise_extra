import pandas as pd


data = pd.read_csv("InfiniumOmni2-5-8_LocusReport.txt",sep="\t")

pos = list(data['Position'])
call_freq = list(data['Call Freq'])

for i in pos:
    if type(i) != float:
        print('Not Float!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

