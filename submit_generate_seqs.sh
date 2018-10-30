#!/bin/bash

set -u
export k=6
export s=1
CONTIG=3000
export IN_DIR="/rsgrps/bhurwitz/mattmiller899/LSTM/ismb2017_lstm/data_${CONTIG}"
export EXT="fasta"
#TYPES=("train" "test")
TYPES=("train")
for i in ${TYPES[@]}; do
    export TYPE=$i
    export P_NAME="gv_unsplit_${CONTIG}_${TYPE}"
    export N_NAME="virus_unsplit_${CONTIG}_${TYPE}"
    ARGS="-q standard -W group_list=bhurwitz -M mattmiller899@email.arizona.edu -m a"
    JOB_ID=`qsub $ARGS -v k,s,P_NAME,N_NAME,TYPE,IN_DIR,EXT -N seqs2ngram -J 1-7 ./run_generate_seqs.sh`
    if [ "${JOB_ID}x" != "x" ]; then
        echo Job: \"$JOB_ID\"
    else
        echo Problem submitting job. Job terminated.
        exit 1
    fi
    echo "job successfully submitted"
done
