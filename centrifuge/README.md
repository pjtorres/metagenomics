# Scripts for analyzing and formating centrifuge data for microbial metagenomics

# Build Docker Image for Centrifuge
```bash
sudo docker build -t cfuge metagenomics/centrifuge/
```

# Make directory for centrifuge output:

```bash
mkdir centri_o
```

# Running Centrifuge using Docker
```bash
docker run -v `pwd`:`pwd` -w `pwd` cfuge centrifuge \
  -x path/to/reference_database/p+h+v \
  -1 in732_2_R1.fastq -2 in732_2_R2.fastq \
  -S centri_o/ in732_2_centrifuge_class.tsv \
  --report-file centri_o/centri_o in732_2.report.tsv 
```
if the above does not work try adding sudo
```bash
sudo docker run -v `pwd`:`pwd` -w `pwd` cfuge centrifuge \
  -x path/to/reference_database/p+h+v \
  -1 file_R1.fastq -2 file_R2.fastq \
  -S centri_o/file_centrifuge_class.tsv \
  --report-file centri_o/file.report.tsv 
```

# Running Docker for python
```bash
docker build -t analysis metagenomics/centrifuge/python/
```
