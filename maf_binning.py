import pandas as pd
pd.set_option("display.precision", 10)

maf_bins = [[], [], [], [], [], [], []]
call_freq_data = pd.read_csv("Call_Freq_Clouard_2022.csv", index_col=[0], low_memory=False)
for i in range(1, len(call_freq_data['Minor_Freq'])+1):
    minor_freq = call_freq_data['Minor_Freq'][i]
    if float(minor_freq) <= 0.02:
        maf_bins[0].append(call_freq_data['Pos'][i])
    elif 0.02 < float(minor_freq) <= 0.04:
        maf_bins[1].append(call_freq_data['Pos'][i])
    elif 0.04 < float(minor_freq) <= 0.06:
        maf_bins[2].append(call_freq_data['Pos'][i])
    elif 0.06 < float(minor_freq) <= 0.10:
        maf_bins[3].append(call_freq_data['Pos'][i])
    elif 0.10 < float(minor_freq) <= 0.20:
        maf_bins[4].append(call_freq_data['Pos'][i])
    elif 0.20 < float(minor_freq) <= 0.40:
        maf_bins[5].append(call_freq_data['Pos'][i])
    elif 0.40 < float(minor_freq) <= 0.5:
        maf_bins[6].append(call_freq_data['Pos'][i])

print(len(maf_bins[0]))
print(len(maf_bins[1]))
print(len(maf_bins[2]))
print(len(maf_bins[3]))
print(len(maf_bins[4]))
print(len(maf_bins[5]))
print(len(maf_bins[6]))

maf_bin_T = pd.DataFrame(maf_bins)
maf_bin = maf_bin_T.T
maf_bin.columns = ['0.00–0.02', '0.02–0.04', '0.04–0.06', '0.06–0.10', '0.10–0.20', '0.20–0.40', '0.40–0.50']
maf_bin.to_csv('MAF_bins.csv')