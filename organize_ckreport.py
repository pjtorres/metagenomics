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


fin=open(inputfile,'r+')
o=open(outputfile+'.txt', 'w')
tax={}
o.write('Genus_species'+'\t'+'Genus_species_strain'+'\t'+'Total'+'\n')
for line in fin:
    if line.split()[3]=='S' and len(line.split())==7 and next(fin).split()[3]=='-':
        if next(fin).split()[3]=='-':
            y= line.split()
            x= next(fin).split()
            taxname=y[-2:]
            species=x[-3:]
            total=float(y[0])+float(x[0])
            taxnamef= ' '.join(taxname)
            specnamef= ' '.join(species)   
            o.write(taxnamef + '\t'+ specnamef+'\t'+str(total)+'\n')
            
o.close()
fin.close()

print ('Done :)')
