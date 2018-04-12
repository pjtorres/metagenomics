#!/usr/bin/python
__author__ = 'Pedro J. Torres'
import os
import sys, getopt
import argparse

'''script removes any samples that have 0 percent hits when outputted in centrifuge using the following scripts
perl centrifuge  -x p+h+v file1.fastq -S file1_centrifuge_class.tsv --report-file file1.report.tsv -5 10 -3 10 -t -p 15

followed by

centrifuge-kreport -x p+h+v file1_centrifuge_class.tsv >  ckreport
'''

#------------Use the command line to take in arguments--------------------------
parser = argparse.ArgumentParser(description='script removes any samples that have 0 percent hits when outputted in centrifuge.')
parser.add_argument('-i','--input', help='Input file is the file that was outputted from centrifuge-kreport',required=True)
parser.add_argument('-o','--output',help='Output file name.', required=False)
args = parser.parse_args()
inputfile= str(args.input) 
outputfile=str(args.output)

fin=open(inputfile, "r+")
o=open(outputfile+' no0.txt','w')
for line in fin:
    line=line.split()
    if line[0] != '0.00':
        newline= ('\t'.join(line))+'\n'
        o.write(newline)
o.close()
fin.close()
print ('done :)')
