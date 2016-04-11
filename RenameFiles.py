
#!/usr/bin/env python3.4
# ---------------------------------------------------------------------------- #
import os, glob
from tqdm import tqdm
# ---------------------------------------------------------------------------- #
os.chdir('../../../../Desktop/')
os.makedirs('../../../../Desktop/Renamed')
# ---------------------------------------------------------------------------- #
'''
def ConvertXLStoCSV():
	XLSFiles = glob.glob('*.xls')
	for file in tqdm(XLSFiles):
		df = pd.read_excel(file)
		df.to_csv('{}.csv'.format(file.strip('.xls')),index=False)
# ---------------------------------------------------------------------------- #
def ConvertXLSXtoCSV():
	XLSXFiles = glob.glob('*.xlsx')
	for file in tqdm(XLSXFiles):
		df = pd.read_excel(file)
		df.to_csv('{}.csv'.format(file.strip('.xlsx')),index=False)
# ---------------------------------------------------------------------------- #
def Upkeep():
	Files = glob.glob('*.xls')
	for Record in Files:
		if bool(re.match('.+.xls',Record,flags=re.I)):
			os.remove(Record)
	Files = glob.glob('*.xlsx')
	for Record in Files:
		if bool(re.match('.+.xlsx',Record,flags=re.I)):
			os.remove(Record)
# ---------------------------------------------------------------------------- #
if __name__ == '__main__':
	ConvertXLStoCSV()
	ConvertXLSXtoCSV()
	Upkeep()
'''