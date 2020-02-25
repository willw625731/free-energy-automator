#!/bin/csh

#SBATCH  -o out/out_batch-h1.o%j
#SBATCH  -e err/err_batch-h1.e%j
#SBATCH  --mail-type=ALL
#SBATCH  --mail-user william.p.wombell@durham.ac.uk
#SBATCH -n 24
#SBATCH -N 1
#SBATCH -p par7.q

module purge
module load slurm/current
module load python/3.6.8

python3.6 /ddn/data/mzkl37/scripts/run_scripts/pvac_glycerin_300K.py

wait

