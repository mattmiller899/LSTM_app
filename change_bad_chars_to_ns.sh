#!/bin/bash
#PBS -l select=1:ncpus=4:mem=24gb
#PBS -l walltime=24:00:00

cd $PBS_O_WORKDIR
TYPES=("train" "test")
ORGS=("girus" "virus")
for i in `seq 1 10`; do
    for j in ${ORGS[@]}; do
        for k in ${TYPES[@]}; do
            INPUT_FILE="./data_PBSIM/${j}_pbsim_${k}_${i}.fastq"
            TMP_FILE="./data_PBSIM/tmp.fastq"
            > $TMP_FILE
            sed 's/[R,Y,S,W,K,M,B,D,H,V]/N/g' ${INPUT_FILE} > ${TMP_FILE}
            mv $TMP_FILE $INPUT_FILE
        done
    done
done
