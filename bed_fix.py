import pandas as pd
import numpy as np
# pd.set_option("display.precision", 10)

data = pd.read_csv("InfiniumOmni2-5-8v1-5_A1.bed",sep="\t")
data = data.drop(['Name'], axis=1)
data = data.loc[data['Chr'] == 'chr20']
to_write = data.to_csv('InfiniumOmni2-5-8_fix.bed',float_format='{:f}'.format,sep='\t', index=False, header=True)