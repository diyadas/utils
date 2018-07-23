# makeigvbatch.py
# by Diya Das; github.com/diyadas
# March 8, 2018

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description =
'''
Usage: makeigvbatch.py --compfile ICAM-OMP.txt --genelist mygenelist.txt
Output: igvbatch_compfile-genelist.txt

Python3 dependencies: numpy, pandas, argparse, pathlib

''', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('--compfile', help="text file containing list of pileups to compare")
parser.add_argument('--genelist', help="text file containing list of genes")
parser.add_argument('--snapdir', help="path to store snapshots")

args = parser.parse_args()

with open(args.compfile) as pileupfile:
    pileuplist = pileupfile.readlines()
with open(args.genelist) as genefile:
    genelist = genefile.readlines()

f = open("igvbatch_" + Path(args.compfile).resolve().stem + '-' + args.genelist, "w")

f.write("new\n")
#f.write("genome mm10\n")
#f.write("expand Refseq genes\n")
f.write("load /Users/diyadas/igv_mm10.xml\n")
f.write("expand \n")
f.write("snapshotDirectory " + args.snapdir + '/'+ Path(args.compfile).resolve().stem + "\n")

for pileup in pileuplist:
    f.write("load " + pileup) 
f.write("\n")

for gene in genelist:
    f.write("goto " + gene) 
    f.write("snapshot " + gene.rstrip() + "_" + Path(args.compfile).resolve().stem + ".png\n")

f.close()
