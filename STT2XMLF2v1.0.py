"""Accepts optional commandline args, returns 2 XML files
"""
import sys
import argparse # see prog.py for usage
import MEDGlobals
import inspect
from CreatePaths import *  # import * may not be best practice
from sys import argv
from GetPhotoPath import FindAndValidateImages
from LocationAdder import NextLocation
from LocationAdder import LastUsedLocation
from MEDFileUtils import CopyPhotosToLocalDrive
from MEDFileUtils import CopyPhotosToSFTP
from MEDUtils import GenerateImageNumberStrings
from DataStructures import DataStructuresFunction
from inspect import currentframe, getframeinfo
from Process import Process

DEFAULT_BATCH_SIZE = 150
DEFAULT_PHOTOS_PER_ITEM = 5
CURRENT_VERSION = argv[0][:-3]
LIVE = True
PRE_PROCESSOR = False
# locate and validate Image files
ImageFolderName = ''
try:
	LogicalDrive = sys.argv[1]  # Test for non G: drives not done 8/15/22
except:
	LogicalDrive = "G:"
ImageFolderName = FindAndValidateImages(LogicalDrive)


Source = SourcePath(ImageFolderName, LogicalDrive)
# check for prior existing files and folders, generate BatchNum, and local image file destination path
LocalDestinationPathValid = False
FullLocalDestinationPathFromGetBatchNum, BatchNum = GetBatchNum(ImageFolderName) # gets BatchNum from STT.txt file and validates
print(f'MSG: Batch Number is: {BatchNum}.  Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
print(f'MSG: Dest Path: {FullLocalDestinationPathFromGetBatchNum}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
FullLocalDestinationPathFromDestinationPath = DestinationPath(ImageFolderName, BatchNum)

if FullLocalDestinationPathFromDestinationPath == FullLocalDestinationPathFromGetBatchNum:
	LocalDestinationPathValid = True
else:
	print(f'Local Destination File Conflict - aborting')
	sys.exit(1)

# We have BatchNum so now can check for and/or create STT.txt file, image SFTP destination path, and XML output files
SpeechToTextFileName = STTtxtFileName(ImageFolderName,BatchNum)
ProceedToCreateSFTPath = DoesDestinationSFTPExist(ImageFolderName, BatchNum)  
# if sftp dest exists then check if STT.txt and XML files exist
FullSFTPDestination = DestinationSFTP(ImageFolderName, BatchNum)

# Name XML output files and Verify they do not already exist
# general XML output file for import to MED site
MEDXMLOutputFileName = ''
MEDSixBitXMLOutputFileName = ''
PandPFSixBitXMLOutputFileName = ''
MEDXMLOutputFileName = MEDXMLFileName(ImageFolderName,BatchNum)

# Intermediate 6Bit XML files i.e. import to 6Bit, export to Etsy
#  this section will be deleted and replaced with calls to WP API and Etsy API and use of XML will be discontinued
MED = False
PandPF = False
MEDOrPandPF = ''
try:
	MEDOrPandPF = sys.argv[2]
except:  # No commandline argument for output so default is MED
	MEDSixBitXMLOutputFileName = SixBitXMLFileName(ImageFolderName,BatchNum)

if MEDOrPandPF == 'MyEarringDepot':
	MEDSixBitXMLOutputFileName = SixBitXMLFileName(ImageFolderName,BatchNum)
	MED = True
elif MEDOrPandPF == 'PandPF':
	PandPFSixBitXMLOutputFileName = PandPFSixBitXMLFileName(ImageFolderName,BatchNum)
	PandPF = True
else:
	MEDSixBitXMLOutputFileName = SixBitXMLFileName(ImageFolderName,BatchNum) # think we got it covered here
	MED = True

# use a list to store these filenames and iterate to check if os.exists
if MED:
	if exists(MEDXMLOutputFileName):
		# log error
		print(f'XML output file {MEDXMLOutputFileName} already exists - aborting')
	if exists(MEDSixBitXMLOutputFileName):
		# log error
		print(f'XML output file {MEDXMLOutputFileName} already exists - aborting')

elif PandPF:
	if exists(PandPFSixBitXMLOutputFileName):
		# log error
		print(f'XML output file {MEDXMLOutputFileName} already exists - aborting')

# Get starting LOCATION and SKU
LastLocation = LastUsedLocation()
print(f'MSG: Last Used Location: {LastLocation}, Module: {argv[0]}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
StartLocation =  NextLocation(LastLocation)
StartSKU = GetStartSKU(ImageFolderName,StartLocation) #returns a COMPLETE sku

#Copy Image files to local drive and SFTP server
print(f'MSG: Starting SKU: {StartSKU}.  Starting Location: {StartLocation}.  Module: {argv[0]}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
print(f'MSG: XML filenames look like: {MEDXMLOutputFileName}. Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
print(f'MSG: Image source path: {Source}, Local Destination: {FullLocalDestinationPathFromDestinationPath}, SFTP Destination: {FullSFTPDestination}, Module: {sys.argv[0]}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
print(f'MSG: Ready to copy Image files.  Module: {sys.argv[0]}: Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')

# implement logging, remove superfluous print commands, place notifications at key milestones
#  NOTIFICATION FORMAT:  print(f'MSG: <msg                          ><Module: {argv[0]}, Line {LineNo}') 
# ***********************************************************************************
# Copy, upload, and backup processes will run as co-routines, relying on asyncio library

CopyPhotosToLocalDrive(Source, FullLocalDestinationPathFromDestinationPath)
CopyPhotosToSFTP(Source, FullSFTPDestination)
#ArchivePhotos(Source, ImageFolderName, BatchNum)

# prepare to ingest and process the STT.txt file and produce the XML output files:
ImageNumberStrings = GenerateImageNumberStrings(DEFAULT_BATCH_SIZE, DEFAULT_PHOTOS_PER_ITEM)


if MED:
	print(f'MSG: MED constant is set. Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
	print(f'MSG: XML output files are: {MEDXMLOutputFileName},{MEDSixBitXMLOutputFileName} Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
	# print(SpeechToTextFileName, StartLocation, StartSKU, ImageNumberStrings, MEDXMLOutputFileName, MEDSixBitXMLOutputFileName)
elif PandPF:
	print(f'PandPF constant is set')
	print(f'XML output files are: {MEDXMLOutputFileName}, {PandPFSixBitXMLOutputFileName}')

print(f'MSG: Checkpoint: Doublecheck all critical vars: Module {__name__}, Line:  {inspect.getframeinfo(inspect.currentframe()).lineno}')
print(f'STT filename:  {SpeechToTextFileName},StartLOCATION: {StartLocation}, StartSKU: {StartSKU} ')
print(FullLocalDestinationPathFromDestinationPath, )
print(f'ImageNumberStrings..., MEDXMLOutputFileName: {MEDXMLOutputFileName}, MEDSixBitXMLOutputFileName: {MEDSixBitXMLOutputFileName}')

# Preprocess STT file => on hold as of 8/22/22
# Process STT file
Process(SpeechToTextFileName, CURRENT_VERSION, StartLocation, StartSKU, ImageNumberStrings, FullLocalDestinationPathFromDestinationPath,
		FullSFTPDestination, DEFAULT_PHOTOS_PER_ITEM, MEDXMLOutputFileName, MEDSixBitXMLOutputFileName, PandPFSixBitXMLOutputFileName, LIVE,PRE_PROCESSOR)
# write XML files

# cleanup - close files, write and close logs. 