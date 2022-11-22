import pandas as pd
import random as rand
data_illumina = pd.read_csv("InfiniumOmni2-5-8_Chr_20.txt", sep='\t')
pos_illumina = data_illumina['Position'].tolist()
data_imp = pd.read_excel("IMP_test.xlsx")
pos = data_imp['POS'].tolist()
t = rand.uniform(0,1)
for i in pos:
    if i in pos_illumina:
        print(i)
        print(type(data_illumina.Position==i))
        x = data_illumina.loc[data_illumina.Position == int(i), 'Call Freq'].values[0]
        print(x)
        if t >= x:
            print('Add Noise')