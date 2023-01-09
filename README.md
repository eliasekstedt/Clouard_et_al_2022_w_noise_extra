# Project Applied Bioinformatics 2022 - Scripts and outputs
**Elias Ekstedt, Philip MacCormack & Klara Solander**

This project is based on the work by Clouard *et al.* 2022, their proposed simulation can be found in the following [GitHub repository](https://github.com/camcl/genotypooler), and their imputation algorithm *Prophaser* can be found in the following [GitHub repository](https://github.com/kausmees/prophaser).

## Scripts
This folder contains the preprocessing scripts created during the project. 

#### Preprocess_locus_rep_v4.py
**_Overview_**

This script takes the chosen locus report and the positions of the markers utilized in the project as input. The output from running this file is a csv file containing all chosen SNPs, their respective call frequencies and minor allele frequencies. One also has the possibility to create a subset of the data, with the size of ones chosing. The purpose of this script is to create a template to be able to add noise within the created pipeline, which can be found in the following [GitHub repository](https://github.com/klso6609/SnakeMake_Clouard_et_al_2022_w_noise).

**_Detailed_**

This script takes the chosen locus report and the positions of the markers utilized in the project as input. In the locus report data, the columns ‘Name’, ‘Chromosome’, ‘AA freq’, ‘AB freq’ and ‘BB freq’ are discarded, leaving a txt file, containing only the position of the SNPs on chromosome 20, their respective call frequencies and minor allele frequencies. All call frequencies of value 1, are given the call frequency 0.999 to account for natural stochasticity in genotype calling. The concordant markers between the preprocessed locus report and the genotype data are identified, and the position, call frequency and minor allele frequency of these are transferred to a txt file. The SNPs in the genotype data which are discordant with those in the preprocessed locus report are given a call frequency of 0.999, and also added to the aforementioned txt file. Thus a txt file containing all chosen markers, with their associated call frequencies is created. 

The creation of the subset follows the principle described above. 

#### imputation_quality.py
**_Overview_**

In this script, each marker is sorted based on minor allele frequency (MAF) into a bin, where the bins have the following intervals - [0 - 0.02], (0.02, 0.04], (0.04, 0.06], (0.06, 0.10], (0.10, 0.20], (0.20, 0.40], (0.40, 0.5]. The intervals chosen are based on those found in Clouard et. al 2022, Table 2. In this, the MAF values are extracted from the Infinium Omni2.5-8 v1.5 Locus Report. Each discrepancy between the real genotypes, i.e. the genotypes pre-imputation and the post-imputation genotypes is counted, for each MAF-bin to which the individual markers have been sorted. From this, a proportion of correctly imputed markers per MAF bin is calculated. The output from this script are tables containing the percentage of correctly imputed genotypes per MAF bin, for each of the six scenarios, i.e Prophaser without noise, Beagle without noise, Prophaser with standard noise, Beagle with standard noise, Prophaser with 0.98 noise intensity and Beagle with 0.98 noise intensity. 

**_Detailed_**

To run these scripts, one must load bioinfo-tools and pysam. In addition to this, one should run the script, requirements.sh, to load PrettyTables and therefore achieve correct output in the tables. 

All post-imputation data from each algorithm is loaded, in addtion to the raw IMP data. These are all converted to dataframes, where in imputation_quality_all.py adds all samples, and imputation_quality.py utilizes only one sample. The raw IMP data is merged with the call frequency data given by Preprocess_locus_rep_v4.py, and bined to achieve a baseline to compare with each bin achieved by the imputed data. Following this, a function is utilized where the input data (the imputed data) is also merged with the call frequency data, binned and then the percentage is calculated by dividing the number of samples per bin with that found when binning the raw data. The results from this are printed in tables directly in the terminal. 

When only running for one sample, i.e. when running imputation_quality.py, the script can be run in the command line. When it comes to 
imputation_quality_all.py, it is recommended to use sbatch to run this. For this reason, there is an additional script, run_imputation_quality.py which facilitates this. 

## Data

#### Call_Freq_Clouard_2022.txt, Call_Freq_subset_Clouard_2022.txt & subset_Clouard_2022.vcf.gz
These are the data files created when running Preprocess_locus_rep_v3.py on the dataset utilized in Clouard *et al.* 2022. The first two are the files containing the call frequencies of the chosen SNPs. The third is the subset of the larger dataset. 

#### Clouard_2022.vcf.gz
The dataset utilized in Clouard *et al.* 2022.

#### kgp_chr20_pos.txt
A file containing only the marker positions, which is utilized in Preprocess_locus_rep_v3.py. This file was created manually by extracting the positions from Clouard_2022.vcf.gz, with the purpose of saving computational time as this file is large and therefore takes time to load and read through. 

### Results

#### Clouard_2022
This folder contains all the intermediate output files and results generated when running the pipeline found given by Clouard *et al.* 2022 without added noise. 

#### Clouard_2022_noise
This folder contains all the intermediate output files and results generated when running the pipeline found given by Clouard *et al.* 2022 using Beagle imputation with standard noise. 

#### Clouard_2022_noise_0.2
This folder contains all the intermediate output files and results generated when running the pipeline found given by Clouard *et al.* 2022 using Beagle imputation with addtional noise intensity of 0.2. 

#### Clouard_2022_noise_0.4
This folder contains all the intermediate output files and results generated when running the pipeline found given by Clouard *et al.* 2022 using Beagle imputation with addtional noise intensity of 0.4. 

#### Clouard_2022_noise_0.6
This folder contains all the intermediate output files and results generated when running the pipeline found given by Clouard *et al.* 2022 using Beagle imputation with addtional noise intensity of 0.6. 

#### Clouard_2022_noise_0.8
This folder contains all the intermediate output files and results generated when running the pipeline found given by Clouard *et al.* 2022 using Beagle imputation with addtional noise intensity of 0.8. 

#### Clouard_2022_noise_1.0
This folder contains all the intermediate output files and results generated when running the pipeline found given by Clouard *et al.* 2022 using Beagle imputation with addtional noise intensity of 1.0. 

#### Prophaser_1_sample
This folder contains all the intermediate output files and results generated when running the pipeline found given by Clouard *et al.* 2022 using prophaser, with only one sample. 

## References 
Clouard C, Ausmees K, Nettelblad C. A joint use of pooling and imputation for genotyping SNPs. BMC Bioinformatics. 2022 Oct 13;23(1):421. doi: 10.1186/s12859-022-04974-7. PMID: 36229780; PMCID: PMC9563787.
