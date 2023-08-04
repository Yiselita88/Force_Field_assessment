#!/bin/bash
#SBATCH --job-name=1GB1_ff14IDPs_autoimage
#SBATCH --output=1GB1_ff14IDPs_md13-18.out
#SBATCH --error=1GB1_ff14IDPs_md13-18.err
#SBATCH --mail-type=ALL
#SBATCH --time=7-00:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=2000
#SBATCH --cpus-per-gpu=1
#SBATCH --gpus-per-task=1
#SBATCH --partition=gpu
#SBATCH --account=alberto.perezant
#SBATCH --qos=alberto.perezant
pwd; hostname; date


echo "parm peptide_sol.prmtop" >> autoimage.in

for i in {1..50}
do
echo "trajin ../heat+MD/md${i}.nc" >> autoimage.in
done


echo "trajout autoimage.nc" >> autoimage.in
echo "autoimage" >> autoimage.in
echo "strip :WAT,Na+,Cl- outprefix strip" >> autoimage.in
echo "go" >> autoimage.in

