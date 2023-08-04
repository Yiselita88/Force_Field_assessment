#!/bin/bash
#SBATCH --job-name=dihedral_phi-psi
#SBATCH --output=dihedral.out
#SBATCH --error=dihedral.err
#SBATCH --mail-type=ALL
#SBATCH --time=7-00:00:00
#SBATCH --ntasks=1
#SBATCH --distribution=cyclic:cyclic
#SBATCH --mem-per-cpu=2000
#SBATCH --account=alberto.perezant
#SBATCH --cpus-per-gpu=1
#SBATCH --gpus-per-task=1
#SBATCH --partition=gpu
#SBATCH --constraint=2080ti

cd $SLURM_SUBMIT_DIR

module load cuda/10.0.130
module load intel/2018.1.163
module load openmpi/4.0.3
module load amber/20

#source ~/.load_Amber

echo "trajin autoimage.nc
dihedral Phi :1@C :2@N :2@CA :2@C out Phi
dihedral Psi :2@N :2@CA :2@C :3@N out Psi" > dih-dia.ptraj
cpptraj strip.peptide_sol.prmtop < dih-dia.ptraj
awk '{print $2}' Phi  > Phi.dat
awk '{print $2}' Psi  > Psi.dat
