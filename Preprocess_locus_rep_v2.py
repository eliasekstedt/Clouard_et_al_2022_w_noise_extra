import pandas as pd
import numpy as np
pd.set_option("display.precision", 10)

epsilon = 1*10**-3

data = pd.read_csv("InfiniumOmni2-5-8_LocusReport.txt",sep="\t")
data = data.loc[data['Chr'] == '20']
data.loc[data['Call Freq'] > 0.999999, 'Call Freq'] = 1-epsilon

pos = pd.read_csv("Pos_imp.txt")
pos = list(pos.iloc[:,0])
dpos = list(data['Position'])

def intersection(dpos, pos):
    lst3 = [value for value in dpos if value in pos]
    return lst3

intersecting = intersection(dpos, pos)
print('No of records intersecting:',len(intersecting))
print('No of records in Illumina Data: ',len(dpos))
print('No of records in Carl Data: ',len(pos))

chr20_filtered = data.query('Position in @intersecting')

with open('InfiniumOmni2-5-8_Chr_20.txt', 'a') as f:
    # dfAsString = chr20_filtered.to_string(header=True, index=False)
    to_write = chr20_filtered.to_csv(sep='\t', index=False, header=True)
    f.write(to_write)
