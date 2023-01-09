#!/bin/bash

ml bioinfo-tools
ml bcftools

bcftools view -s NA19472,HG00650,HG01746 IMP.chr20.pooled.snps.gl.vcf.gz > filtered.vcf



 

