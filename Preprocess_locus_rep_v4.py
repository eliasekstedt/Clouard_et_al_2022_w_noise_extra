import pandas as pd
import random

# Setting precision for the float variables and defining the random seed for choosing a subsample of 1000 SNPs
pd.set_option("display.precision", 10)
random.seed(10)

# Defining epsilon
epsilon = 1*10**-3

# Reading in the Locus Report for Infinium Omni 2-5-8 and extracting chr20, and the appropriate fields
locus_data = pd.read_csv("InfiniumOmni2-5-8v1-5_A1_LocusReport.txt", sep="\t", index_col=[0], low_memory=False)
locus_data = locus_data.loc[locus_data['Chr'] == '20']
locus_data = locus_data.drop(['Name', 'Chr', 'AA Freq', 'AB Freq', 'BB Freq'], axis=1)
locus_data.loc[locus_data['Call Freq'] > 0.999999, 'Call Freq'] = 1-epsilon
locus_data_list = list(locus_data['Position'])

#Reading in the positions of the markers in dataset utilized in Clouard et al. 2022
kgp_chr20 = pd.read_csv("kgp_chr20_pos.txt")
kgp_chr20_list = list(kgp_chr20.iloc[:, 0])

# # Creating a subset of 1000 markers for testing
index = random.sample(range(1, len(kgp_chr20)), 1000)
for i in range(1000):
    kgp_chr20_subset = kgp_chr20.loc[index]
kgp_chr20_subset_list = list(kgp_chr20_subset.iloc[:, 0])

# # Identifying the concordant markers between the Locus Report and Clouard et al. 2022 dataset
intersecting = pd.Series(list(set(kgp_chr20_list) & set(locus_data_list)))


# # Identifying the concordant markers between the Locus Report and the 1000 marker subset
# # of the Clouard et al. 2022 dataset
intersecting_subset = pd.Series(list(set(kgp_chr20_subset_list) & set(locus_data_list)))

print('No of markers in Locus Report: ',len(locus_data_list))
print('No of markers in Clouard et al. 2022 dataset: ',len(kgp_chr20_list))
print('No of markers intersecting (Locus Report - Clouard et al. 2022):', len(intersecting))
print('No of markers intersecting (Locus Report - subset):', len(intersecting_subset))

# Creating dataframe of positions and call frequencies,
# where markers not found in the locus rapport are given Call Freq = (1 - epsilon)
call_freq_list = [['Position', 'Call_Freq', 'Minor_Freq']]
for position_kgp in kgp_chr20_list:
    if position_kgp in intersecting.values.tolist():
        call_freq_list.append([int(position_kgp), locus_data.loc[locus_data['Position'] == position_kgp, 'Call Freq'].tolist()[0], locus_data.loc[locus_data['Position'] == position_kgp, 'Minor Freq'].tolist()[0]])
    else:
        call_freq_list.append([int(position_kgp), float(1-epsilon), int(0)])
call_freq = pd.DataFrame(call_freq_list[1:], columns=['Pos', 'Call_Freq', 'Minor_Freq'])
# print(call_freq)

# Creating dataframe of positions and call frequencies for the subset,
# where markers not found in the locus rapport are given Call Freq = (1 - epsilon)
call_freq_subset_list = [['Position', 'Call_Freq', 'Minor_Freq']]
for position_kgp in kgp_chr20_subset_list:
    if position_kgp in intersecting_subset.values.tolist():
        call_freq_subset_list.append([int(position_kgp), locus_data.loc[locus_data['Position'] == position_kgp, 'Call Freq'].tolist()[0], locus_data.loc[locus_data['Position'] == position_kgp, 'Minor Freq'].tolist()[0]])
    else:
        call_freq_subset_list.append([int(position_kgp), float(1-epsilon), int(0)])

call_freq_subset = pd.DataFrame(call_freq_subset_list[1:], columns=['Pos', 'Call_Freq', 'Minor_Freq'])

# Converting dataframe of positions and call frequencies to csv file
call_freq[1:].to_csv('Call_Freq_Clouard_2022.csv')
call_freq_subset[1:].to_csv('Call_Freq_subset_Clouard_2022.csv')

