import pandas as pd
import io
import os




kgp_chr20 = pd.read_excel('data/Big_data/Clouard_2022.xlsm')
kgp_chr20_subset = pd.read_csv('Call_Freq_Clouard_2022.csv')

discordant = [element for element in kgp_chr20['POS'] if element not in kgp_chr20_subset['Position']]

for position in discordant:
    kgp_chr20.drop(kgp_chr20.Position == position, axis=0)

kgp_chr20.to_csv('Clouard_subset_2022.csv')
