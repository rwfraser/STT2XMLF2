"""accepts argv[1] 4 char string for next photofolder date, argv[2] 2 char string for current batch number
    do not run reset with no args or parameters, results will be unpredictable
"""
# requires at least 3 photo folders be present in DCIM
import os
import datetime
import inspect
from sys import argv
from os.path import exists
from inspect import currentframe, getframeinfo


'''
configfile = 'config.rst'
if not exists(configfile):
	with open(configfile, 'w') as config:
		dateString = '0233'
		BatchNum = '01'
		config.write(dateString)
		config.write(BatchNum)
		config.close()
elif exists(configfile):
	with open(configfile, 'r') as config:
		dateString = config.readline()
		BatchNum = config.readline()
		config.close()
'''
# rename existing photosfolder
path = 'C:\\DCIM\\'
ManualDateString = argv[1]
NewFileName = '100_' + ManualDateString
dest = path + NewFileName
photosfolders = os.listdir(path)
try:
	source = path + photosfolders[2]
except:
	print(f'Only one photo folder present - it will be renamed')
	source = path + photosfolders[0] #

os.rename(source,  dest)

YEAR = '2022'

# rename existing STT.txt file
ManualBatchNum = argv[2]
NewSTTFileName = YEAR + ManualDateString + ManualBatchNum + 'STT.txt'
print(f'MSG: New STT File name is: {NewSTTFileName}; Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
cwdfiles = os.listdir()
for file in cwdfiles:
	dotindex = file.find('.')
	# print(f' file is: {file}')
	if file[dotindex-3:dotindex] == 'STT':
		# print(f' file is: {file}')
		oldSTTFilename = file
os.rename(oldSTTFilename, NewSTTFileName)

'''code for config file 
if dateString == '':
	dateString = '0232'
if BatchNum == '':
	BatchNum = '01'
# increment dateString
if dateString[0] == '0':
	dateString = '0' + str((int(dateString) + 1))
elif dateString[0] == '1':
	dateString = int(dateString)
else:
	print(f'MSG: Error: Too many Months in date.  Module: {_name__}, Line 49')


if int(BatchNum == 4):
	BatchNum = 1
else:
	BatchNum = int(BatchNum) + 1
# store config file
BatchNum = '0' + str(BatchNum)
dateString = str(dateString)
with open(configfile,'w') as config:
	config.write(dateString)
	config.write('\n')
	config.write(BatchNum)
	config.close()
'''


