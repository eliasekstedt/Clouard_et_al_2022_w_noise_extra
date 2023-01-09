# Importing the relevant packages
import pysam
import pandas as pd
import itertools
from prettytable import PrettyTable

# Reading the data files
call_freq_data = pd.read_csv("Call_Freq_Clouard_2022.csv", index_col=[0], low_memory=False)
without_noise_original = pysam.VariantFile("IMP.chr20.snps.gt.vcf.gz")

without_noise_imputed_original_beagle = pysam.VariantFile("/proj/snic2019-8-216/private/Applied_Bioinformatics/MAF_bin_evaluation/No_Noise_Beagle/IMP.chr20.pooled.imputed.vcf.gz")
standard_noise_imputed_original_beagle = pysam.VariantFile("/proj/snic2019-8-216/private/Applied_Bioinformatics/MAF_bin_evaluation/Standard_Noise_Beagle/IMP.chr20.pooled.imputed.vcf.gz")
high_noise_imputed_original_beagle = pysam.VariantFile("/proj/snic2019-8-216/private/Applied_Bioinformatics/MAF_bin_evaluation/High_Noise_Beagle/IMP.chr20.pooled.imputed.vcf.gz")

without_noise_imputed_original_prophaser = pysam.VariantFile("/proj/snic2019-8-216/private/Applied_Bioinformatics/MAF_bin_evaluation/No_Noise_Prophaser/IMP.chr20.pooled.imputed.vcf.gz")
standard_noise_imputed_original_prophaser = pysam.VariantFile("/proj/snic2019-8-216/private/Applied_Bioinformatics/MAF_bin_evaluation/Standard_Noise_Prophaser/IMP.chr20.pooled.imputed.vcf.gz")
high_noise_imputed_original_prophaser = pysam.VariantFile("/proj/snic2019-8-216/private/Applied_Bioinformatics/MAF_bin_evaluation/High_Noise_Prophaser/IMP.chr20.pooled.imputed.vcf.gz")

# Creating list of sample names
sample_names= ['HG01063','HG03518','NA07048','HG01808','NA20790','NA19000','NA18979','NA18631','HG01685','NA12872','HG03159','NA18507','HG02049','NA21101','HG02890','NA20287','HG03370','HG02023','HG03238','HG03611','HG03774','NA19144','HG02734','NA19099','HG03767','NA18868','NA19676','HG01932','HG02250','HG00108','NA19068','HG02053','HG01092','HG03437','HG00403','NA18933','HG02006','HG00707','NA19700','NA18612','NA18965','HG03077','HG03775','HG00266','NA18967','HG02678','HG04033','HG00366','NA19430','HG03781','HG02058','HG03603','HG02047','HG01589','NA19916','NA19070','NA18645','HG03882','NA21133','NA19789','HG01325','HG00332','HG03770','HG00475','NA18856','NA18981','NA19750','NA18617','HG01783','HG01510','NA20527','HG01447','HG03193','HG03470','HG01029','HG00731','NA18636','HG03866','HG03303','NA12272','HG03907','HG04039','HG03803','HG00116','HG01789','HG01985','HG01182','NA20862','HG00879','NA19438','NA19759','HG02485','NA18941','HG03955','HG01623','HG01669','HG01348','HG03072','HG02502','HG01082','HG02155','NA18950','HG01797','HG04202','NA19984','NA20321','HG03163','NA20502','NA19922','NA20412','HG03679','HG01768','NA20753','HG00235','NA11843','HG03109','NA18562','HG03698','HG01785','NA19027','HG02786','NA19456','NA20892','HG00360','HG00708','HG03382','HG01871','HG02817','NA19092','HG00736','HG03103','HG02187','HG02266','HG03085','HG03950','HG02142','HG02253','HG04038','HG02768','NA20828','HG01142','HG02470','HG01927','HG02314','HG03720','HG02878','HG04238','HG04017','HG00583','HG01513','NA19434','HG03917','HG03112','HG00328','HG02154','HG01356','NA11932','HG00356','HG00684','HG00693','HG01939','HG01795','HG04099','NA19429','NA18953','HG04047','NA19726','HG02649','NA21142','NA20808','HG03446','HG00463','HG01536','HG02009','HG00364','HG03589','HG03060','NA19731','HG01626','HG00099','HG03594','HG03746','HG01886','HG03598','NA19720','HG04140','HG02508','NA12003','HG00436','HG02685','NA19648','HG00345','NA20511','HG03097','HG03625','HG01205','HG03115','NA20281','HG02648','HG01680','HG01918','HG03040','NA18986','NA19085','HG02156','HG01861','HG01170','HG03850','HG04090','HG03401','NA18508','HG01133','HG03235','NA20891','NA20856','HG00437','NA20866','HG03711','HG03844','HG01920','NA19057','HG03995','HG02557','HG03660','NA19017','HG01874','HG02256','NA19310','HG01679','HG00123','NA19901','NA19403','NA20531','HG03782','NA12751','HG02309','NA19472','HG00650','HG01746','HG03862']

# Creating dataframe of position, sample and genotype for each entry, for each datafile
without_noise_original_list = []
for rec in without_noise_original.fetch():
    for sample in sample_names:
        without_noise_original_list.append([rec.pos, sample, rec.samples[sample]['GT']])
without_noise = pd.DataFrame(without_noise_original_list, columns=['Pos', 'Sample', 'GT'])

#Beagle
without_noise_original_imputed_list_beagle = []
for rec in without_noise_imputed_original_beagle.fetch():
    for sample in sample_names:
        without_noise_original_imputed_list_beagle.append([rec.pos, sample, rec.samples[sample]['GT']])
without_noise_imputed_beagle = pd.DataFrame(without_noise_original_imputed_list_beagle, columns=['Pos', 'Sample', 'GT'])

standard_noise_original_imputed_list_beagle = []
for rec in standard_noise_imputed_original_beagle.fetch():
    for sample in sample_names:
        standard_noise_original_imputed_list_beagle.append([rec.pos, sample, rec.samples[sample]['GT']])
standard_noise_imputed_beagle = pd.DataFrame(standard_noise_original_imputed_list_beagle, columns=['Pos', 'Sample', 'GT'])

high_noise_original_imputed_list_beagle = []
for rec in high_noise_imputed_original_beagle.fetch():
    for sample in sample_names:
        high_noise_original_imputed_list_beagle.append([rec.pos, sample, rec.samples[sample]['GT']])
high_noise_imputed_beagle = pd.DataFrame(high_noise_original_imputed_list_beagle, columns=['Pos', 'Sample', 'GT'])

#Prophaser
without_noise_original_imputed_list_prophaser = []
for rec in without_noise_imputed_original_prophaser.fetch():
    for sample in sample_names:
        without_noise_original_imputed_list_prophaser.append([rec.pos, sample, rec.samples[sample]['GT']])
without_noise_imputed_prophaser = pd.DataFrame(without_noise_original_imputed_list_prophaser, columns=['Pos', 'Sample', 'GT'])

standard_noise_original_imputed_list_prophaser = []
for rec in standard_noise_imputed_original_prophaser.fetch():
    for sample in sample_names:
        standard_noise_original_imputed_list_prophaser.append([rec.pos, sample, rec.samples[sample]['GT']])
standard_noise_imputed_prophaser = pd.DataFrame(standard_noise_original_imputed_list_prophaser, columns=['Pos', 'Sample', 'GT'])

high_noise_original_imputed_list_prophaser = []
for rec in high_noise_imputed_original_prophaser.fetch():
    for sample in sample_names:
        high_noise_original_imputed_list_prophaser.append([rec.pos, sample, rec.samples[sample]['GT']])
high_noise_imputed_prophaser = pd.DataFrame(high_noise_original_imputed_list_prophaser, columns=['Pos', 'Sample', 'GT'])

# Merging files
without_noise_call_freq = without_noise.merge(call_freq_data, on='Pos', how='inner', indicator=False)

without_noise_call_freq.loc[without_noise_call_freq['Minor_Freq'].between(0, 0.02, 'both'), 'Bin'] = '[0.00, 0.02]'
without_noise_call_freq.loc[without_noise_call_freq['Minor_Freq'].between(0.02, 0.04, 'right'), 'Bin'] = '[0.02, 0.04]'
without_noise_call_freq.loc[without_noise_call_freq['Minor_Freq'].between(0.04, 0.06, 'right'), 'Bin'] = '[0.04, 0.06]'
without_noise_call_freq.loc[without_noise_call_freq['Minor_Freq'].between(0.06, 0.10, 'right'), 'Bin'] = '[0.06, 0.10]'
without_noise_call_freq.loc[without_noise_call_freq['Minor_Freq'].between(0.10, 0.20, 'right'), 'Bin'] = '[0.10, 0.20]'
without_noise_call_freq.loc[without_noise_call_freq['Minor_Freq'].between(0.20, 0.40, 'right'), 'Bin'] = '[0.20, 0.40]'
without_noise_call_freq.loc[without_noise_call_freq['Minor_Freq'].between(0.40, 0.50, 'right'), 'Bin'] = '[0.40, 0.50]'

def maf_binning(input_data):
    combined_imputed_data = input_data.merge(without_noise, how = 'inner' ,indicator=False)
    combined_call_freq = combined_imputed_data.merge(call_freq_data, on='Pos', how='inner', indicator=False)

    combined_call_freq.loc[combined_call_freq['Minor_Freq'].between(0, 0.02, 'both'), 'Bin'] = '[0.00, 0.02]'
    combined_call_freq.loc[combined_call_freq['Minor_Freq'].between(0.02, 0.04, 'right'), 'Bin'] = '[0.02, 0.04]'
    combined_call_freq.loc[combined_call_freq['Minor_Freq'].between(0.04, 0.06, 'right'), 'Bin'] = '[0.04, 0.06]'
    combined_call_freq.loc[combined_call_freq['Minor_Freq'].between(0.06, 0.10, 'right'), 'Bin'] = '[0.06, 0.10]'
    combined_call_freq.loc[combined_call_freq['Minor_Freq'].between(0.10, 0.20, 'right'), 'Bin'] = '[0.10, 0.20]'
    combined_call_freq.loc[combined_call_freq['Minor_Freq'].between(0.20, 0.40, 'right'), 'Bin'] = '[0.20, 0.40]'
    combined_call_freq.loc[combined_call_freq['Minor_Freq'].between(0.40, 0.50, 'right'), 'Bin'] = '[0.40, 0.50]'

    bin1 = combined_call_freq.Bin.value_counts()['[0.00, 0.02]'] / (without_noise_call_freq.Bin.value_counts()['[0.00, 0.02]'])
    bin2 = combined_call_freq.Bin.value_counts()['[0.02, 0.04]'] / (without_noise_call_freq.Bin.value_counts()['[0.02, 0.04]'])
    bin3 = combined_call_freq.Bin.value_counts()['[0.04, 0.06]'] / (without_noise_call_freq.Bin.value_counts()['[0.04, 0.06]'])
    bin4 = combined_call_freq.Bin.value_counts()['[0.06, 0.10]'] / (without_noise_call_freq.Bin.value_counts()['[0.06, 0.10]'])
    bin5 = combined_call_freq.Bin.value_counts()['[0.10, 0.20]'] / (without_noise_call_freq.Bin.value_counts()['[0.10, 0.20]'])
    bin6 = combined_call_freq.Bin.value_counts()['[0.20, 0.40]'] / (without_noise_call_freq.Bin.value_counts()['[0.20, 0.40]'])
    bin7 = combined_call_freq.Bin.value_counts()['[0.40, 0.50]'] / (without_noise_call_freq.Bin.value_counts()['[0.40, 0.50]'])

    x = PrettyTable()
    x.field_names = ['MAF bin', 'Proportion correct genotyped']
    x.add_row(['[0.00, 0.02]', round(bin1, 3)])
    x.add_row(['[0.02, 0.04]', round(bin2, 3)])
    x.add_row(['[0.04, 0.06]', round(bin3, 3)])
    x.add_row(['[0.06, 0.10]', round(bin4, 3)])
    x.add_row(['[0.10, 0.20]', round(bin5, 3)])
    x.add_row(['[0.20, 0.40]', round(bin6, 3)])
    x.add_row(['[0.40, 0.50]', round(bin7, 3)])
    print(x)

print('NO NOISE BEAGLE')
maf_binning(without_noise_imputed_beagle)

print('NO NOISE PROPHASER')
maf_binning(without_noise_imputed_prophaser)

print('STANDARD NOISE BEAGLE')
maf_binning(standard_noise_imputed_beagle)

print('STANDARD NOISE PROPHASER')
maf_binning(without_noise_imputed_prophaser)

print('HIGH NOISE BEAGLE')
maf_binning(high_noise_imputed_beagle)

print('HIGH NOISE PROPHASER')
maf_binning(high_noise_imputed_prophaser)
