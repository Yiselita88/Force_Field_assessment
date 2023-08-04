#!/bin/bash
#SBATCH --job-name=1GB1_ff14IDPsFF_analysis
#SBATCH --output=1GB1_ff14IDPsFF_analysis.out
#SBATCH --error=1GB1_ff14IDPsFF_analysis.err
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


module purge
module load  cuda/11.1.0 nvhpc/20.11 openmpi/4.0.5 amber/20


cpptraj -i /orange/alberto.perezant/yisel/script_analysis/autoimage.in
cpptraj -i /orange/alberto.perezant/yisel/script_analysis/rmsd.in
cpptraj -i /orange/alberto.perezant/yisel/script_analysis/dihedral.in
cpptraj -i /orange/alberto.perezant/yisel/script_analysis/rog.in
cpptraj -i /orange/alberto.perezant/yisel/script_analysis/end2end.in
cpptraj -i /orange/alberto.perezant/yisel/script_analysis/rmsf.in
cpptraj -i /orange/alberto.perezant/yisel/script_analysis/phipsi.in
cpptraj -i /orange/alberto.perezant/yisel/script_analysis/ab.in
