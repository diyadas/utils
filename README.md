# utils

useful little tools & code snippets without a home


- `qv` : utility to get usage info / core availability for SGE cluster ; replace "compute" with string that identifies queues
- `md5-recursive` : notes on getting checksums for all files within Linux / macOS directories and mechanism for comparison; written for the case when different file structures exist on machines (some bash, some Python)

### Getting sequencing data from GEO
1. `getGEOmd.py` : get metadata for an experiment given a BioProject ID (found on GEO record, format is PRJNAXXXXXX)
2. `getGEOfastq.sh` : given metadata / ID file, get fastq for each sample from SRA (assumes paired-end)

