# bdgnormz.py
# by Diya Das; github.com/diyadas
# February 27, 2018

import numpy as np
import pandas as pd
import subprocess
import os.path
import argparse

parser = argparse.ArgumentParser(description = 
'''

Python3 dependencies: numpy, pandas, argparse 

''', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-bdgfile', help="bedgraph file")

args = parser.parse_args()


chr2keep = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8',
       'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15',
       'chr16', 'chr17', 'chr18', 'chr19', 'chrX']

bedgraph_data = pd.read_csv(args.bdgfile, header=None, names=['chr','start','stop','coverage'],sep="\t")
bedgraph_data = bedgraph_data[bedgraph_data['chr'].isin(chr2keep)]
int_len = bedgraph_data['stop'] - bedgraph_data['start']
N = int_len.sum()
mean = np.sum(int_len * bedgraph_data['coverage'])/N
sd = np.sqrt(np.sum((bedgraph_data['coverage'] -mean)**2*int_len)/(N-1))
print(mean)
print(sd)
bedgraph_data['coverage'] = (bedgraph_data['coverage'] - mean)/sd
#print (bedgraph_data)
bedgraph_data.to_csv(args.mdfile, index=False, sep="\t")