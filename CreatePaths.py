import os
import sys
import paramiko
import inspect
from os.path import exists
from inspect import currentframe, getframeinfo

# Local libraries to be imported when incorporated into project modules:
# import MEDGlobals
# from LocationAdder import NextLocation

# future MEDGlobal vars/constants
# YEAR, USER, DefaultLocalDrive all belong in MEDGlobals when module becomes available
YEAR = '2022' # upgrade this to use current year as provided by system time
DEFAULT_USER = os.environ['USERNAME']
DefaultLocalDrive = "C:"

# vars for local testing purposes
PhotosFolder = '100_0102'
BatchNum = '01'

def GetLocalDestinationPathStub(PhotosFolder):
	"""accepts string, returns string LocalDestinationPathStub
	"""
	# this function does NOT sub '-'' for '_' (to support 6Bit)
	username = ''
	YEAR4Stub = YEAR + '\\'
	Month = PhotosFolder[4:6] + '\\'
	Day = PhotosFolder[6:] + '\\'
	LocalDrivePathStub = DefaultLocalDrive + '\\' + 'users\\' 
	username = DEFAULT_USER + '\\' 
	LocalDestinationPathStub = LocalDrivePathStub + username + YEAR4Stub + Month + Day
	return LocalDestinationPathStub  # includes Month and Day but not hyphenation

def GetBatchNum(PhotosFolder):
	"""Accepts a string, returns a 2 character string, and a local path
	    Earrings are processed in batches of 30, batch count is reset daily, theoretical daily batch max  = 99
	    In practice, logic will only be written for BatchNum < 10 i.e. single digit
	    This function i) gets current BatchNum from STT.txt file ii) checks for existence of BatchNum-1 same day batch
	    iii) checks for existence of BatchNum dest folder
	    If BatchNum - 1 same day batch doesn't exist - throws warning, if BatchNum dest folder exists exits with error(1) 
	    Returns the validated current BatchNum and/or a warning
	"""
	# i)
	MaxBatches = 4 # arbitrary maximum daily batches 8/18/22
	# get expected current BatchNum from STT.txt file
	PhotosFolderModified = PhotosFolder.replace('_','-') # to support 6Bit
	LocalDrivePathStub = GetLocalDestinationPathStub(PhotosFolder)
	TodaysSTTFilesList = []
	BatchNumFromSTTFile = ''

	FileList = os.listdir()
	for file in FileList: # find today's STT file(s)
		DotLocation = file.find('.')
		if (file[DotLocation-3:DotLocation] == 'STT') and file[0:8] == (YEAR + PhotosFolder[4:6] + PhotosFolder[6:]):
			TodaysSTTFilesList.append(file)
	# iterate through todays STT files and find the most recent batch
	MostRecent = ''
	for file in TodaysSTTFilesList:
		print(f'MSG: STT.txt File Name is: {file}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
		if file[8:10] > MostRecent[8:10]:
			MostRecent = file 
	BatchNumFromSTTFile  = MostRecent[8:10]
	print(f'MSG: Batch # from STT file is: {BatchNumFromSTTFile}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno} ')
	# provided correct STT file exists preceding code works.  Validation code below is not tested. 08/20/22 

	'''
	# check if there is already an existing BatchNum folder, throw an error if so, else return the correct BatchNum 
	# search for up to 3 previous batches - more than 4 batches per day exceeds current daily limit 08/15/22
	for i in range(MaxBatches, 0, -1):  # descending iteration to find any existing batches
		LocalBatchNum = '0' + str(i) + '\\' # BatchNum is returned and reused in main() so cannot be modified directly
		FullLocalDestinationPath = LocalDrivePathStub + LocalBatchNum +  PhotosFolderModified
		if (i == MaxBatches) and (os.path.exists(FullLocalDestinationPath)):  # daily max exceeded 
			print(f'MSG: Fatal error - Batches > 4. Module: {__name__}, inspect.getframeinfo(inspect.currentframe()).lineno')
			sys.exit(1)
		elif os.path.exists(FullLocalDestinationPath):  # i < 4, we have ith previous batches. Validate and exit
			FullLocalDestinationPath = LocalDrivePathStub  + LocalBatchNum +  PhotosFolderModified #construct return Path
			if LocalBatchNum == BatchNumFromSTTFile: # passes validation checks
					BatchNum = LocalBatchNum	# update BatchNum
					print(f'MSG: Returning {BatchNum} as BatchNum, {FullLocalDestinationPath} as Dest Path, Module  {__name__}, inspect.getframeinfo(inspect.currentframe()).lineno')
					return FullLocalDestinationPath, BatchNum 
	# we have not exit(1) or return, so no previous Batch exists.  Validate and return
	FullLocalDestinationPath = LocalDrivePathStub  + LocalBatchNum +  PhotosFolderModified #construct return Path
	LocalBatchNum = '01'
	if LocalBatchNum == BatchNumFromSTTFile: # passes validation checks
		BatchNum = LocalBatchNum
		print(f'MSG: Returning {BatchNum} as BatchNum, {FullLocalDestinationPath} as Dest Path, Module  {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
		return FullLocalDestinationPath, BatchNum  # if first batch of the day
	'''
	BatchNum = BatchNumFromSTTFile
	LocalBatchNum = BatchNum + '\\'
	FullLocalDestinationPath = LocalDrivePathStub + LocalBatchNum + PhotosFolderModified
	print(f'MSG: Returning {BatchNum} as BatchNum, Local Dest. Path: {FullLocalDestinationPath}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
	return FullLocalDestinationPath, BatchNum  # if first batch of the day

def SourcePath(PhotosFolder, LogicalDrive='G:'):
	"""Accepts two strings, returns the complete path to the photos source folder
	"""
	# source path is G:\DCIM\PhotosFolder
	FullSourcePath = LogicalDrive +'\\DCIM\\' + PhotosFolder
	return FullSourcePath


def DestinationPath(PhotosFolder, BatchNum):
	"""Accepts two strings, returns complete local destination path for photos
	"""
	# Local Destination Path is C:\users\%username%\%year%\%month%\%day%\BatchNum\PhotosFolderModified
	LocalDrivePathStub = DefaultLocalDrive + '\\' + 'users\\' 
	username = DEFAULT_USER + '\\' 
	YEAR4Stub = YEAR + '\\'
	Month = PhotosFolder[4:6] + '\\'
	Day = PhotosFolder[6:] + '\\'
	BatchNum = BatchNum + '\\'
	PhotosFolderModified = PhotosFolder.replace('_','-')
	FullLocalDestinationPath = LocalDrivePathStub + username + YEAR4Stub + Month + Day + BatchNum +  PhotosFolderModified
	if not os.path.exists(FullLocalDestinationPath): # BUG: pre-existing batch #4 is not the only reason this may fail
		print(f'MSG: Destination path is:  {FullLocalDestinationPath}, Module {__name__}, Line:  {inspect.getframeinfo(inspect.currentframe()).lineno}')
		return FullLocalDestinationPath
	else:  
		print(f'MSG: Fatal error - Destination folder already exists. Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
		sys.exit(1)

def DoesDestinationSFTPExist(PhotosFolder,BatchNum):
	"""accepts two strings, returns Fatal error status if dest sftp path already exists - this is a serious error
	"""

	LOCAL_PATH_ROOT = "C:\\users\\RogerIdaho\\"
	SFTP_SERVER = "rogeridaho.sftp.wpengine.com"
	SFTP_ROOT = "./wp-content/uploads/"
	SFTP_ACCOUNT = "rogeridaho"
	SFTP_PASSWORD = "Cyb4rS4cur1ty!!##"  # should be secured via environment variable in VM
	SFTP_PORT = 2222
	SFTP_PROTOCOL = "SFTP"
	YEAR4SFTP = YEAR + '/'
	Month = PhotosFolder[4:6] + '/'
	Day = PhotosFolder[6:] + '/'
	BatchNum = BatchNum + '/'
	SFTPDestination = SFTP_ROOT + YEAR4SFTP + Month + Day + BatchNum[:-1]

	# check if destination path already exists, if so send abort message to main()
	transport = paramiko.Transport((SFTP_SERVER, SFTP_PORT))
	password = SFTP_PASSWORD
	username = SFTP_ACCOUNT
	transport.connect(username=username, password=password)
	if transport.connect:
		print(f"MSG: SFTP Connection established.  Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}")
		sftp = paramiko.SFTPClient.from_transport(transport)
		try:
			sftp.listdir(SFTPDestination)
			print(f'MSG: ERROR destination SFTP path already exists - aborting.  Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
		except:
			print(f'MSG: Dest SFTP not present, clear to proceed.  Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
			sftp.close()
			transport.close()
			return
	# check for existence of STT.txt, XML files and log if they exist (they should exist if sftp dest exists)
	sftp.close()
	transport.close()
	sys.exit(0)


	if stfp.listdir(SFTPDestination):
		print(f'MSG: ERROR destination SFTP path already exists - aborting.  Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
		sys.exit(1)

def DestinationSFTP(PhotosFolder, BatchNum):
	"""Accepts two strings, returns SFTP destination path
	"""

	LOCAL_PATH_ROOT = "C:\\users\\RogerIdaho\\"
	SFTP_SERVER = "rogeridaho.sftp.wpengine.com"
	SFTP_ROOT = "./wp-content/uploads/"
	SFTP_ACCOUNT = "rogeridaho"
	SFTP_PASSWORD = "Cyb4rS4cur1ty!!##"  # should be secured via environment variable in VM
	SFTP_PORT = 2222
	SFTP_PROTOCOL = "SFTP"
	YEAR4SFTP = YEAR + '/'
	Month = PhotosFolder[4:6] + '/'
	Day = PhotosFolder[6:] + '/'
	BatchNum = BatchNum + '/'

	
	
	SFTPDestination = SFTP_ROOT + YEAR4SFTP + Month + Day + BatchNum[:-1]
	print(f'MSG: SFTP DEST PATH:  {SFTPDestination}, Module: {__name__}, Line:  {inspect.getframeinfo(inspect.currentframe()).lineno}')
	
	# proceed to create destination path
	transport = paramiko.Transport((SFTP_SERVER, SFTP_PORT))
	password = SFTP_PASSWORD
	username = SFTP_ACCOUNT
	transport.connect(username=username, password=password)

	if transport.connect:
		print(f"MSG: SFTP Connection established.  Module {__name__}, Line:  {inspect.getframeinfo(inspect.currentframe()).lineno}")
		sftp = paramiko.SFTPClient.from_transport(transport)
		try:
			sftp.chdir(SFTP_ROOT)
		except:
			print(f'Can not change to wp-content/uploads/ - remove trailing /')
			sys.exit(1)
		try:
			sftp.chdir(YEAR)
		except:
			print(f'Cannot change to {YEAR} folder')
			sys.exit(1)
		'''  Update and test this code by Y/E 22, also insert breaks where
			     necessary to avoid superfluous sub-folder creation
			sftp.mkdir(YEAR[:-1])
			sftp.chdir(YEAR[:-1])
			sftp.mkdir(Month[:-1])
			sftp.chdir(Month[:-1])
			sftp.mkdir(Day[:-1])
			sftp.chdir(Day[:-1])
			sftp.mkdir(BatchNum[:-1])
			sftp.chdir(BatchNum[:-1])
			break
		'''
		print(f'MSG: Creating SFTP path {SFTPDestination}.  Module: {__name__}, Line:  {inspect.getframeinfo(inspect.currentframe()).lineno}')
		try:
			sftp.chdir(Month[:-1])
		except:
			sftp.mkdir(Month[:-1])
			sftp.chdir(Month[:-1])
			sftp.mkdir(Day[:-1])
			sftp.chdir(Day[:-1])
			sftp.mkdir(BatchNum[:-1])
			sftp.chdir(BatchNum[:-1])
		try:
			sftp.chdir(Day[:-1])
		except:
			sftp.mkdir(Day[:-1])
			sftp.chdir(Day[:-1])
			sftp.mkdir(BatchNum[:-1])
			sftp.chdir(BatchNum[:-1])

	print(f'MSG: Path {SFTPDestination} create complete - please verify, Module {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
	sftp.close()
	transport.close()
	return SFTPDestination


def StartLOCATION(LastUsedLocation):
	"""Accepts a string, returns starting LOCATION string
	"""
	# Add 1 to LastUsedLocation to return startingLOCATION string
	# this routine is located at from LocationAdder import NextLocation

def GetStartSKU(PhotosFolder, StartLOCATION):
	"""Accepts two strings, returns starting SKU string
	"""
	# SKU structure is YYYYMMDDLOCATION000
	StartSKU = YEAR + PhotosFolder[4:] + StartLOCATION + '000'
	return StartSKU

def STTtxtFileName(PhotosFolder,BatchNum):
	"""Accepts two strings, returns the expected STT.txt filename
	"""
	#  the speech to text data file naming convention is: YYYYMMDDSTT.txt
	STTtxtFileName = YEAR + PhotosFolder[4:] + BatchNum + 'STT.txt'
	if exists(STTtxtFileName):
		return STTtxtFileName
	else:
		print(f'MSG: Cannot locate STT.txt file: {STTtxtFileName} - aborting.  Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
		sys.exit(1)

def  MEDXMLFileName(PhotosFolder,BatchNum):
	"""Accepts two strings, returns the MED website XML filename
	"""
	MEDXMLFileName = YEAR + PhotosFolder[4:] + BatchNum + 'MED' + '.xml'
	return MEDXMLFileName
	

def SixBitXMLFileName(PhotosFolder,BatchNum):
	"""Accepts two strings, returns the 6Bit XML filename for MED Etsy store
	"""
	SixBitXMLFileName = YEAR + PhotosFolder[4:] + BatchNum + '6BitMED' + '.xml'
	return SixBitXMLFileName

def PandPFSixBitXMLFileName(PhotosFolder, BatchNum):
	"""Accepts two strings, returns the 6Bit XML filename for PandPF Etsy store
	"""
	PandPFSixBitXMLFileName = YEAR + PhotosFolder[4:] + BatchNum + '6BitPandPF' + '.xml'
	return PandPFSixBitXMLFileName 

def ArchivePhotos(PhotosFolder):
	pass