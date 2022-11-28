import io
import os
import pandas as pd
import vcf

vcf_reader = vcf.Reader(open('data/Big_data/Clouard_2022.vcf', 'r'))

for record in vcf_reader:
    print(record)