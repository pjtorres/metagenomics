#!/usr/bin/python
__author__= 'Pedro J. Torres <pjtorres88@gmail.com> 2018'
import argparse
import os

"Script will sum up your centrifuge output into an otu style format"
#---------- Split to count the number of hits given by a blast output and make an OTU style format------
parser=argparse.ArgumentParser(description="Script will combine multiple of your organized centrifuge output into a single file.. Also make sure all your centrifuge outputs you want to summarize are in their own directory")
parser.add_argument('-d','--dir', help='This directory wil contrain all your samples after the "mpa2final.py" script is run. All text files should be in one directory. Add directory here or leave blank for current working firectory', required=True)
parser.add_argument('-o','--out', help='Name of summary ouput text file', required=True)
args=parser.parse_args()
directory_i=str(args.dir)
o_file=str(args.out)

#----check to see if you input you input the directory where files are kept---------------
if args.dir is None:
    directory=str(os.getcwd())
    directory=directory+"/"
else:
    cwd=str(os.getcwd())
    cwd=cwd+"/"
    directory=cwd+directory_i

#-----------------Make dictionary and call each txt file in directory-------------------------------
"""make dictionary to keep track of your taxonomy and counts for each file. Keys are going to be taxa name and a list will keep track of the abundance for each file"""
taxa={}
headers=[]
# All txt files (should be blast output txt files) in current directory are added to a list 'F'
F=[i for i in os.listdir(directory) if i.split(".")[-1]=="txt"]
print ("You are combining " +str(len(F))+" text Files")
cwd=str(os.getcwd())
d=cwd+"/"+directory_i+"/"

#------------Call and open each txt file in directory and start reading each line which should be taxonomy/gene name---------
for txt in F:
    f=open(txt,"r")
    header=f.readline()
    headers.append(header)
    for line in f:
       # print line
        line=line.strip()
        line=line.split()
        abund=line[-1] #abundance accompanying the taxonomic lineages
        taxaLin=line[:-1]
        taxaLin=' '.join(taxaLin) # taxonomic full lineage
        #taxa[taxaLin]=str(abund)
        """Add taxa/gene as key in dictionary and its value is a list in which each element represents taxa/gene count for each file.Checks to see if Taxa is already in the dictionary, if not, it will add it and and start to makes a list with a zero to keep count each time it sees that taxa it will add 1."""
        if taxaLin not in taxa:
            taxa[taxaLin]=[0]*len(F)# Make a list for to keep the Taxa abundace for each file in directory or length of F.
        else:pass
        taxa[taxaLin][F.index(txt)]=str(abund)
print ("There are a total of " +str(len(taxa)) +" taxa")

"""Above it does two things. First it will be calling the values to the Key 'taxName'. But because there are a list of counters (one for each file) we need to tell it which one. By indexing all the files in 'txt' you keep everything in order, call the right list index and add 1 each time you see that taxaName in that particular file."""

#-----------------Create new output file and write in abundance
o=open(o_file,"w+")
o.write("Taxa\t"+"\t".join(F)+"\n")
for i in taxa:
    o.write(i+"\t"+"\t".join([str(xx) for xx in taxa[i]])+"\n")
o.close()

print ("Done :)")
