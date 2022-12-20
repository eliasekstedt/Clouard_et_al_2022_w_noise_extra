"""
The purpose of this code is to be able to evaluate the effects of noise on the data set, with the different imputation algorithms
"""

# Importing the relevant packages
import pandas as pd

# Reading the data file without noise
without_noise_original = pd.read_excel('IMP.chr20.snps.gt.SMALL.NOISE.xlsx', header=[259], usecols=lambda x: 'Unnamed' not in x)
without_noise_proc = without_noise_original.drop(['#CHROM', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT'], axis=1)
header_list = []
for col in without_noise_proc.columns[1:]:
    header_list.append(col)
without_noise_list = []
for row in range(len(without_noise_proc.axes[0])):
   for col in range(len(without_noise_proc.axes[1])):
    without_noise_list.append([header_list[col], without_noise_proc.loc[row]['POS'], without_noise_proc.loc[row][col]])

without_noise = pd.DataFrame(without_noise_list, columns=['SAMPLE', 'POS', 'GENOTYPE'])


# # Reading the data file after imputation, without noise
# without_noise_imputation_original = pd.read_excel('EXCEL_IMPUTERING_UTAN_NOISE', header=[259], usecols=lambda x: 'Unnamed' not in x)
# without_noise_imputation = without_noise_imputation_original.drop(['#CHROM', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT'], axis=1)

# # Reading the data file with noise
# with_noise_original = pd.read_excel('EXCEL_MED_NOISE', header=[259], usecols=lambda x: 'Unnamed' not in x)
# with_noise = with_noise_original.drop(['#CHROM', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT'], axis=1)

# # Reading the data file after imputation, with noise
# with_noise_imputation_original = pd.read_excel('EXCEL_IMPUTERING_MED_NOISE', header=[259], usecols=lambda x: 'Unnamed' not in x)
# with_noise_imputation = with_noise_imputation_original.drop(['#CHROM', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT'], axis=1)


# # Removing duplicates, which means that the output is the diffences between the datasets 
# diff_without_noise = pd.concat([without_noise, without_noise_imputation_original]).drop_duplicates(subset = ['SAMPLE', 'POS' 'GENOTYPE'], keep=False)
# diff_with_noise = pd.concat([with_noise, with_noise_imputation_original]).drop_duplicates(subset = ['SAMPLE', 'POS' 'GENOTYPE'], keep=False)


# # Creating MAF bins to sort the markers
# maf_bins_temp = [[], [], [], [], [], [], []]
# call_freq_data = pd.read_csv("Call_Freq_Clouard_2022.csv", index_col=[0], low_memory=False)
# for i in range(1, len(call_freq_data['Minor_Freq'])+1):
#     minor_freq = without_noise['Minor_Freq'][i]
#     if float(minor_freq) <= 0.02:                              # The number of entries in each bin without added noise
#         maf_bins_temp[0].append(int(call_freq_data['Pos'][i])) # 14249
#     elif 0.02 < float(minor_freq) <= 0.04:
#         maf_bins_temp[1].append(int(call_freq_data['Pos'][i])) # 4855
#     elif 0.04 < float(minor_freq) <= 0.06:
#         maf_bins_temp[2].append(int(call_freq_data['Pos'][i])) # 2781
#     elif 0.06 < float(minor_freq) <= 0.10:
#         maf_bins_temp[3].append(int(call_freq_data['Pos'][i])) # 4576
#     elif 0.10 < float(minor_freq) <= 0.20:
#         maf_bins_temp[4].append(int(call_freq_data['Pos'][i])) # 8558
#     elif 0.20 < float(minor_freq) <= 0.40:
#         maf_bins_temp[5].append(int(call_freq_data['Pos'][i])) # 12203
#     elif 0.40 < float(minor_freq) <= 0.5:
#         maf_bins_temp[6].append(int(call_freq_data['Pos'][i])) # 5473

# print(len(maf_bins_temp[0]))
# print(len(maf_bins_temp[1]))
# print(len(maf_bins_temp[2]))
# print(len(maf_bins_temp[3]))
# print(len(maf_bins_temp[4]))
# print(len(maf_bins_temp[5]))
# print(len(maf_bins_temp[6]))

# maf_bin_T_temp = pd.DataFrame(maf_bins_temp)
# maf_bin_temp = maf_bin_T_temp.T
# maf_bin_temp.columns = ['1'], ['2'], ['3'], ['4'], ['0.10, 0.20'], ['0.20, 0.40'], ['0.40, 0.50']
# #                       ['0.00, 0.02'], ['0.02, 0.04'], ['0.04, 0.06'], ['0.06, 0.10'], ['0.10, 0.20'], ['0.20, 0.40'], ['0.40, 0.50']

# def maf_bin_sorting(input_data, sorting_df):
#     maf_bins = [[], [], [], [], [], [], []]
#     for SNP in input_data: 
#         for marker in range(len(sorting_df)): 
#             bin = sorting_df[sorting_df == SNP['POS']].dropna(axis=1, how='all').columns.tolist()
#             maf_bins[int(bin)].append([SNP['POS'], SNP['SAMPLE'], SNP['GENOTYPE']])
#     bin1 = 1 -(int(len(maf_bins[0])) / 14249)
#     bin2 = 1- (int(len(maf_bins[1])) / 4855)
#     bin3 = 1 - (int(len(maf_bins[2])) / 2781)
#     bin4 = 1 - (int(len(maf_bins[3])) / 4576)
#     bin5 = 1 - (int(len(maf_bins[4])) / 8558)
#     bin6 = 1 - (int(len(maf_bins[5])) / 12203)
#     bin7 = 1 - (int(len(maf_bins[6])) / 5473)

#     print(bin1)
#     print(bin2)
#     print(bin3)
#     print(bin4)
#     print(bin5)
#     print(bin6)
#     print(bin7)
    




