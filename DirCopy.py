#!/usr/bin/env python3
import os
import csv

missing = []
moved = []
notFound = []

def main():
	curdir = os.listdir()
	toRead = [x for x in curdir if x.endswith('.csv')][0]#takes first csv it finds in current dir

	with open(toRead) as csvf:
		readCSV = csv.reader(csvf, delimiter=',')
		for row in readCSV:
			raw = row[3].split('\\',6)[-1]#splits dir
			missing.append(raw)
			

	for i in missing:
		if os.path.isfile(i):
			lpath = i.split('\\')
			filename = lpath[-1]
			mpath = lpath[0:-1]
			mpath.insert(0,'TOTRANSFER')#creates dir in same dir, recreates all dirs within this one
			mpath = '\\'.join(mpath)
			if os.path.exists(mpath):
				pass
			else:
				os.makedirs(mpath)
			os.rename(i,mpath+'\\'+filename)
			moved.append(i)
			
		else:
			notFound.append(i)
	with open('log.txt', 'w') as f:
		f.write('-Found and Moved-\n')
		if moved:
			for i in moved:
				f.write(i+'\n')
		else:
			f.write('None\n')
		f.write('\n-Not Found-\n')
		if notFound:
			for i in notFound:
				f.write(i+'\n')
		else:
			f.write('None')

if __name__ == '__main__':
	main()
