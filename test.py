import random as rand
import pandas as pd


data = pd.read_csv("data/Call_Freq_Clouard_2022.txt", sep="\t", index_col=[0], low_memory=False)

print(data['Call_Freq'].mean())