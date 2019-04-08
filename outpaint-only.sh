#!/bin/bash                                                                     
#SBATCH -N 1                                                                    
#SBATCH -n 1
##SBATCH --mem-per-cpu 60000                                                                    
##SBATCH -p physicsgpu1                                                            
#SBATCH -p asinghargpu1
##SBATCH -p sulcgpu1
##SBATCH -p cidsegpu1                                                          
#SBATCH -q wildfire                                                             
#SBATCH --gres=gpu:1                                                            
#SBATCH -t 0-48:00                                                               
##SBATCH -o slurm.%j.${1}.out                                                   
##SBATCH -e slurm.%j.${1}.err                                                    
#SBATCH --mail-type=END,FAIL                                                   
#SBATCH --mail-user=ksuthar1@asu.edu                                           
                                                                                                       
module load tensorflow/1.8-agave-gpu
module unload python/.2.7.14-tf18-gpu

python3.6 outpaint-only.py