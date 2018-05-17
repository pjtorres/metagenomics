#!/bin/bash
#$ -cwd

#prior to running this script you might want ot filter your centrifuge_class.tsv file first. I filter it based on the hit length. If 150
#bp sequence reads then I fiter to anythiing over 100bp. 
#awk ‘$6 >=100’ file1_centrifuge_class.tsv > file1_centrifuge_class_filtered.tsv

FILE=$(head -n $SGE_TASK_ID all_reads.txt | tail -n 1)
NAME=$(echo $FILE | cut -d'.' -f1)

perl /home3/torres/centrifuge/centrifuge-kreport -x /home3/torres/centrifuge/p+h+v $FILE > $NAME.ckreport.tsv
