#!/bin/bash
#SBATCH -A uppmax2022-3-1
#SBATCH -M snowy
#SBATCH -p core -n 8
#SBATCH -J imputation_quality_beagle_high_noise
#SBATCH -t 3:00:00

module load python/3.9.5
module load bioinfo-tools
module load pysam

python imputation_quality_all.py
