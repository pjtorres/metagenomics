#!/usr/bin/python
__author__= 'Pedro J. Torres <pjtorres88@gmail.com> 2018'
import re,os
import argparse

#-----------Command Line Arguments-----------------
parser=argparse.ArgumentParser(description="Script allows you to convert your centrifuge output into a format that only includes top strain and full taxonomic lineage.")
parser.add_argument('-i','--input', help='Input tsv file from kraken2mpa',required=True)
parser.add_argument('-o','--out', help='Name of output file: e.g., "sample1_final"', required=True)

args = parser.parse_args()
o_file=str(args.out)
inputfile=str(args.input)

fin=open(inputfile, 'r+')
tmp1=inputfile+'tmp.txt'
fout=open(tmp1, 'w+')

#-- this part of the script will get rid of anything that does not have taxonomic information of species and above----
taxa=['s_Homo sapiens']
abund={}
for line in fin:
    if len(line.split('|')) >=7: # allows you to only focus on data with information of species and above
        line =  line.replace('\t','|')
        if line.count('s_')==2 and len(line.split('|')) ==9 :pass #allows you to skip some of the repetitive regions in the data
        else:
            fout.write(line)
            species=line.split('|')[6]
            if species not in taxa:
                taxa.append(species)
    if re.search('s_synthetic construct',line):
        fout.write(line)

fin.close()
fout.close()

fin2=open(tmp1, 'r+')

#-- Seting up our dictionary to hold the taxa name up to strain if possible and that species clads abundance----
#-- line_num will allow us to replace the original key name -that will hold the up to the species name and  -----
#--replace it with the strain name when possible ------
final={}
line_num=0

#-- start looping through the lines in our file and only focusing on those lines that go up to the species name, thus
#--- the 8 you see below
for line in fin2:
    if len(line.split('|'))==8:
        strain_n=[] #List will hold the names of the different strains anytime it loops into a new genus and
        line_num+=1
        count=0.0
        count+=float(line.split('|')[-1])
        k_s=line.split('|')[:-1] # print from kingdom to phylum
        strain_1=k_s
        indiv= strain_1[6]
        final[('|'.join(k_s))]=count
        if re.search('p_Unclassified_reads', line):
            k_s=line.split('|')
            un= k_s[:-1]
            strain_1='|'.join(un)
            unnum=k_s[-1].strip()
            unclassified=strain_1
            if float(unnum)>float(0):
                final[strain_1]=float(unnum)

#--this allows you to see if the current species in the loop it has any strains associated with it which we can
#--then add to our final output
    if len(line.split('|'))>8 and re.search(indiv,line):
        line2= line.split('|')[-2]
        strain_n.append(line2)
       # print strain_n[:2] # this is if I want two strains I will leave it as one
        first_strain = strain_n[0]
        while len(k_s)< 8: # here we make sure to add only the first and highest abundance strain for a particular species to the list
            k_s.append(first_strain)
            strain_1='|'.join(k_s)
            
#-- some organism have both a species and strain name others only have a species and no strain name. The following
#-- script makes sure if it does have a strain name then we remove the organisms name which only goes up to species
        for key,value in final.items():
            new = key.split('|')[:7]
            new2='|'.join(new)
            strain_renew=strain_1.split('|')[:7]
            strain_renew='|'.join(strain_renew)
            if new2 == strain_renew:
                final[strain_1]= final.pop(key)
    if re.search('s_synthetic construct', line):
        syncon_total = float(line.split()[-1])
        syncon_name= " ".join((line.split()[:2]))
        final[syncon_name] = syncon_total

#--get our final total for our dictionary values
total = sum(final.values())
print total, final.get(unclassified)
#--write into a new file
out=o_file+'.txt'
o=open(o_file,'w+')
o.write('Taxa '+ '\t'+'Relative_Abundance'+'\n')
for i in final:
    final_2=(float(final[i])/total)*100
    final_2 =  round(final_2,2)
    o.write(i+ '\t' + str(final_2)+'\n')
o.close()
fin2.close()
cwd = os.getcwd()
rm_tmp=cwd+'/'+tmp1
os.remove(rm_tmp)

print ('DONE :)')
