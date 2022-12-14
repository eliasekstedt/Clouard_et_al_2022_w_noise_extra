# Project Applied Bioinformatics 2022 - Scripts and outputs
**Elias Ekstedt, Philip MacCormack & Klara Solander**

This project is based on the work by Clouard *et al.* 2022, their proposed simulation can be found in the following [GitHub repository](https://github.com/camcl/genotypooler), and their imputation algorithm *Prophaser* can be found in the following [GitHub repository](https://github.com/kausmees/prophaser).

## Scripts
This folder contains the preprocessing scripts created during the project. 

#### Preprocess_locus_rep_v3.py
**_Overview_**

This script takes the chosen locus report and the positions of the markers utilized in the project as input. The output from running this file is a csv file containing all chosen SNPs, and their respective call frequencies. One also has the possibility to create a subset of the data, with the size of ones chosing. The purpose of this script is to create a template to be able to add noise within the created pipeline, which can be found in the following [GitHub repository](https://github.com/klso6609/Applied-Bioinformatics).

**_Detailed_**

This script takes the chosen locus report and the positions of the markers utilized in the project as input. In the locus report data, the columns ‘Name’, ‘Chromosome’, ‘AA freq’, ‘AB freq’, ‘BB freq’ and ‘Minor Freq’ are discarded, leaving a txt file, containing only the position of the SNPs on chromosome 20 and their respective call frequency. All call frequencies of value 1, are given the call frequency 0.999 to account for natural stochasticity in genotype calling. The concordant markers between the preprocessed locus report and the genotype data are identified, and the position and call frequency of these are transferred to a txt file. The SNPs in the genotype data which are discordant with those in the preprocessed locus report are given a call frequency of 0.999, and also added to the aforementioned txt file. Thus a txt file containing all chosen markers, with their associated call frequencies is created. 

The creation of the subset follows the principle described above. 

## Data

#### Call_Freq_Clouard_2022.txt, Call_Freq_subset_Clouard_2022.txt & subset_Clouard_2022.vcf.gz
These are the data files created when running Preprocess_locus_rep_v3.py on the dataset utilized in Clouard *et al.* 2022. The first two are the files containing the call frequencies of the chosen SNPs. The third is the subset of the larger dataset. 

#### Clouard_2022.vcf.gz
The dataset utilized in Clouard *et al.* 2022.

#### kgp_chr20_pos.txt
A file containing only the marker positions, which is utilized in Preprocess_locus_rep_v3.py. This is file was created manually by extracting the positions from Clouard_2022.vcf.gz, with the purpose of saving computational time as this file is large and therefore takes time to load and read through. 

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
