#!/bin/bash
#$ -cwd

# Set up variables for all the files ---------
FILE=$(head -n $SGE_TASK_ID R1.txt | tail -n 1)
FILER=$(head -n $SGE_TASK_ID R2.txt | tail -n 1)
NAME=$(echo $FILE | cut -d'_' -f1,2)

perl /home3/torres/centrifuge/centrifuge -x /home3/torres/centrifuge/p+h+v -1 $FILE -2 $FILER -S centri_o/$NAME.centrifuge_class.tsv --report-file centri_o/$NAME.report.tsv  -5 10 -3 10
