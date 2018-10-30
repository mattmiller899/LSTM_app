#!/bin/bash

set -u
ARGS="-q standard -W group_list=bhurwitz -M mattmiller899@email.arizona.edu -m a"
JOB_ID=`qsub $ARGS -N RemoveBadChars ./change_bad_chars_to_ns.sh`
if [ "${JOB_ID}x" != "x" ]; then
    echo Job: \"$JOB_ID\"
else
    echo Problem submitting job. Job terminated.
    exit 1
fi
echo "job successfully submitted"
