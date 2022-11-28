import pandas as pd
import random as rand
call_freq_data = pd.read_csv("data/Call_Freq_subset_Clouard_2022.txt", sep='\t')
pos_call_freq_data = call_freq_data['Position'].tolist()
data_clouard = pd.read_csv("data/Small_data/Clouard_subset_2022.txt")
pos = data_clouard['Position'].tolist()
r = rand.uniform(0,1)
for pos in pos:
    if pos in pos_call_freq_data:
        print(pos)
        call_freq = call_freq_data.loc[call_freq_data.Position == int(pos), 'Call Freq'].values[0]
        print(  call_freq)
        if r >= call_freq:
            print('Add Noise')