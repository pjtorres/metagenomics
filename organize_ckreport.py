#!/usr/bin/python
__author__ = 'Pedro J. Torres'
import os
import sys, getopt
import argparse

'''This script takes the output file from rmv_0_creport.py and organizes it to only show bacterial genus, species, strain and abudnance'''

#------------Use the command line to take in arguments--------------------------
parser = argparse.ArgumentParser(description='This script takes the output file from rmv_0_creport.py. Will only show top strain not all strains identified in centrifuge')
parser.add_argument('-i','--input', help='Input file name aka the output file from running "python rmv_o_creport.py"',required=True)
parser.add_argument('-o','--output',help='Output directory name.', required=False)
args = parser.parse_args()
inputfile= str(args.input)
outputfile=str(args.output)

with open(inputfile,'r+') as f:
    for line in f:
        if line.split()[3]=='S' and len(line.split())==7:
            x= ''.join(islice(f,1))
            x= x.split()
            c=0
            if x[3]=='-':
                mvx= '\t'.join(x)
                mvx=mvx.split()
                line = line.split() 
                bac_spec=' '.join(line[-2:])
                strain=''.join(mvx[-1:])
                total=float(line[0])+float(mvx[0])
                o.write(bac_spec+'\t'+bac_spec+" " +str(strain)+'\t'+str(total)+'\n')

            else:pass
        
o.close()
print ('Done :)')
