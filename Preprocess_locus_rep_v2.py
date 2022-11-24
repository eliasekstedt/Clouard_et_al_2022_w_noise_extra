import pandas as pd
import numpy as np
pd.set_option("display.precision", 10)

epsilon = 1*10**-3

data = pd.read_csv("InfiniumOmni2-5-8_LocusReport.txt",sep="\t")
data = data.loc[data['Chr'] == '20']
data = data.drop(['Index', 'AA Freq', 'AB Freq', 'BB Freq', 'Minor Freq'], axis=1)
data.loc[data['Call Freq'] > 0.999999, 'Call Freq'] = 1-epsilon

pos = pd.read_csv("Pos_imp_big.txt")
pos = list(pos.iloc[:,0])
dpos = list(data['Position'])

intersecting = set(pos).intersection(dpos)
print('No of records intersecting:',len(intersecting))
print('No of records in Illumina Data: ',len(dpos))
print('No of records in Carl Data: ',len(pos))

chr20_filtered = data.query('Position in @intersecting')
# chr20_filtered['Position'] = chr20_filtered['Position'].astype(float)
chr20_filtered['Position'] = chr20_filtered['Position']
to_write = chr20_filtered.to_csv('InfiniumOmni2-5-8_Chr_20.txt',float_format='{:f}'.format,sep='\t', index=False, header=True)
