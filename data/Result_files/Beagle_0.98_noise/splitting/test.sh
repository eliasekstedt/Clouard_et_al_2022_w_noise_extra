#!/bin/bash

file='../beagle_samples/IMP.chr20.pooled.imputed.vcf.gz'

#bcftools query -l $file | wc -l
#bcftools query -l $file

bcftools query -f '%POS\n' $file | wc -l
bcftools query -f '%POS\n' $file > imputed_markers_pos.txt
