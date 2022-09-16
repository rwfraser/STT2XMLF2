def FindAndValidateImages(drive="G:"):
	"""Locates and validates drive, folder, and image files.
	Accepts optional drive string and returns validated images folder name
	"""
	# only worthwhile error checking will be implemented. i.e. G:\DCIM path is assumed.  
	#  if it cannot be found we abort, error is too serious to survive further execution
	import re
	import os
	import pathlib
	import shutil
	import sys
	import inspect
	import MEDGlobals
	from sys import argv
	from os.path import exists
	from inspect import currentframe, getframeinfo

	# assume we are working with an SD card in drive G:
	LogicalDrive = drive
	# LogicalDrive = "G:" 
	# we are looking for a DCIM folder containing photos
	PathToPhotoDir = LogicalDrive + "\\DCIM"
	Thumbsdotdb = 'Thumbs.db'

	# verify DCIM folder exists on card in G: drive or abort
	# scan the DCIM folder and locate the most recent photo folder
	DirContents = []
	try:
		DirContents = os.listdir(PathToPhotoDir)
		print(f'MSG: Folders Found in {PathToPhotoDir}: {DirContents}. Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
	except:
		print(f'MSG: Cannot find DCIM folder on Drive {LogicalDrive}. Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
		sys.exit(1)

	# We have found DCIM (or aborted with fatal error).  
	# for files in dircontents, extract a sorted list of photofolders:
	#  name format:  DDD_DDDD.  Sort by last four DDDD digits
	ValidPhotoFolders = []
	ValidFile = ''
	for file in DirContents:
		ValidFile = re.match('\d\d\d_\d\d\d\d', file)
		if ValidFile:
			ValidPhotoFolders.append(ValidFile[0])
	ValidPhotoFolders.sort(reverse=True)
	MostRecentPhotosFolder = ''
	for folder in ValidPhotoFolders:
		if folder[4:8] > MostRecentPhotosFolder[4:8]:  # compares the last four digit data strings only, 3 digit  
			                                           #  prefixes (i.e. 100, 101) are ignored. If there are multiple
			                                           #  folders with the same date, but different prefixes the folder
			                                           #  with the largest prefix will be selected.
			MostRecentPhotosFolder = folder


	# validate it is not newer than today's date
	'''
	if int(MostRecentPhotos[:-4]> now()):
		raise warning
	'''

	BatchNum = 1 # default batch number - see GetBatchNum for detection of prior same-day batches

	# now validate its contents s/b 150 .jpeg files  numbered consecutively from 1-150
	PathToPhotosFolder = PathToPhotoDir + "\\" + str(MostRecentPhotosFolder)
	PhotoFilesList = os.listdir(PathToPhotosFolder)
	# check for .jpgs only
	RemoveThumbsDb = False
	for file in PhotoFilesList:
		# print(file)
		if file[8:12] != '.JPG':
			print(f'WARNING: non-jpg file(s) detected')
			if file == Thumbsdotdb:
				RemoveThumbsDb = True
				print(f'Superfluous file is thumbs.db and will be removed')
			else:
				print(f'Unknown superfluous file detected - see session log') # raise warning that superfluous file exists 
				# print all files which are not .jpg to session log
	if RemoveThumbsDb:
		PhotoFilesList.remove(Thumbsdotdb)
		try:
			os.remove(Thumbsdotdb)
		except:
			print(f'MSG: Could not remove Thumbs.db. Module {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')

	# file list is curated, now check for its length
	if len(PhotoFilesList) != 150:  # this should be set as a GLOBAL constant
		print(f'MSG: WARNING: Incorrect number of files.  Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
	PhotoFilesList.sort() # sort ordinally then extract the number of the first file, format:  IMG_NNNN.jpg
	tempCheck = int(PhotoFilesList[0][4:8])
	if tempCheck == 1:
		tempCheck = int(tempCheck)
		# print(f'Selected chars are: {tempCheck}')
	else:
		print(f'Error detected - check photfile numbering. Program aborted')
		sys.exit(1)
	
	# sort files list and then check for ordinal correctness
	counter = 1
	for file in PhotoFilesList:
		FileNumber = int(file[4:8])
		if FileNumber != counter:
			print(f'file number is: {int(file[4:8])}, count is {counter}')
		else:
			pass
			# print(f'filename: {file}, count: {counter}')
		counter+=1

	# Correct photo folder and the PhotoFilesList are now validated.
	# LOG THIS INFO: print(f'Tests and Validation passed for {MostRecentPhotosFolder}')
	# print(f'{argv[0]} Line 117: Most recent images folder is: {MostRecentPhotosFolder}')
	print(f'MSG: Images Folder is: {MostRecentPhotosFolder}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
	return MostRecentPhotosFolder
