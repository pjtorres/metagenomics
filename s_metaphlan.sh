#!/bin/bash
#$ -cwd

# script allows for multiple fastq files to be converted to fasta. Done on clsuter. Will need to add the names of all file you want to 
# convert into fasta into a new txt file here named 'fastq_files.txt'. Thenn submit in qsub -t 1-#:1 

#calls the bowtie i need
source ~/.bashrc 

FILE=$(head -n $SGE_TASK_ID meta.txt | tail -n 1)

~/miniconda2/bin/python ~/biobakery-metaphlan2-40d1bf693089/biobakery-metaphlan2-v1/metaphlan2.py $FILE  --input_type fastq > ${FILE%.fastq}.metaphlan_profile.txt
