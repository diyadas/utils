# getGEOmd.py
# by Diya Das; github.com/diyadas
# February 24, 2018

import pandas as pd
import subprocess
import xml.etree.ElementTree as ET
import os.path
import argparse

parser = argparse.ArgumentParser(description = 
'''This script returns metadata for each sample given a BioProject ID, or a file containing the BioSample IDs. 
If a BioProject ID is supplied, the samplefile containing the SRR, SRX, and SAMN IDs will be written to a file with the specified filename; 
otherwise, the samplefile will be assumed to already contain this data.''')

parser.add_argument('-bioproject', help="PRJNAXXXXXX; supply if no samplefile exists")
parser.add_argument('-samplefile', help="Owner_SRR_SRX_SAMNID.txt; Run,Experiment,BioSample ID file")
parser.add_argument('-mdfile', help="Owner_MD.txt; file to save metadata to")

args = parser.parse_args()

if args.bioproject is None and os.path.isfile(samplefile):
	raise SystemExit("You haven't supplied a BioProject ID and your samplefile does not exist. Please check your inputs.")

if args.bioproject is not None:
	subprocess.run(['esearch -db sra -query '+ args.bioproject +' | efetch --format runinfo | cut -d"," -f1,11,26 > '+ args.samplefile], shell=True, stdout=subprocess.PIPE)

def process_sample(entry):
	"""
	This function executes a query of the biosample database and returns all "attributes" by name.
	"""
	biosample = entry['BioSample']
	result = subprocess.run(['esearch -db biosample -query '+ biosample +' | efetch --format xml'], shell=True, stdout=subprocess.PIPE)
	xml = result.stdout
	tree = ET.ElementTree(ET.fromstring(xml))
	root = tree.getroot()
	attributes = root.find('BioSample').find('Attributes')
	for property in attributes:
		entry[property.attrib['attribute_name']] = property.text
	return entry

sample_info = pd.read_csv(args.samplefile)
sample_info = sample_info.apply(process_sample, axis = 1)
sample_info.to_csv(args.mdfile, index=False)
