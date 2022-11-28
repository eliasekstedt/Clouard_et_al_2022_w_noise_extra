import pandas as pd


data = pd.read_csv("InfiniumOmni2-5-8_LocusReport.txt",sep="\t")
data = data.loc[data['Chr'] == '20']
print('No records in Chromosome 20: ',len(data))

