#!/bin/bash

usage="Usage: $(basename "$0") metadata_file.csv \n\n
This script takes as input the result of geoGEOmd.py \n
Requirements: prior installation of the sra-toolkit: https://www.ncbi.nlm.nih.gov/sra/docs/toolkitsoft/ \n
"

if [ "$1" == "-h" ]; then
  echo "\n\t"$usage
  exit 0
fi

 
log_file="${1%.*}_"$(date +"%m%d%Y-%H%M%S")".log"

mkdir -p fastq

for SRRID in $(tail -n+2 $1 | cut -d"," -f1 ); do 
echo $SRRID  | tee -a "$log_file"
if [ ! -e 'fastq/'$SRRID'_1.fastq' ] | [ ! -e 'fastq/'$SRRID'_2.fastq' ]
then
    fastq-dump --outdir fastq/ -I --split-files $SRRID | tee -a "$log_file" && rm $HOME/ncbi/public/sra/*.sra* && echo "successfully downloaded "$SRRID | tee -a "$log_file"
fi
done
