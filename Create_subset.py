import pandas as pd

kgp_chr20 = pd.read_excel('data/Clouard_2022.xlsx')
kgp_chr20 = kgp_chr20[5:]
kgp_chr20.rename(columns={'Unnamed: 1':'Position'}, inplace=True)
kgp_chr20_subset = pd.read_csv('data/Call_Freq_subset_Clouard_2022.txt',sep='\t')

pos_in_kgp_chr20_subset = kgp_chr20_subset.Position.unique()
merged_chr20 = kgp_chr20[kgp_chr20['Position'].isin(pos_in_kgp_chr20_subset)]

merged_chr20.rename(columns={'Position':'Unnamed: 1'}, inplace=True)
merged_chr20.to_csv('Clouard_subset_2022.txt',sep='\t', index=False, header=True)
