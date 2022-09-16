"""Synchronous File copying functions
"""
import sys
import shutil
import paramiko
import pysftp
import time
import os
import inspect
from inspect import getframeinfo, currentframe


def CopyPhotosToLocalDrive(source, destination):
    """accepts two strings, copies image files from SD to local drive, returns exit(0) for success, exit(1) for failure
    """
#    LocalDestination = (LOCAL_PATH_ROOT + YEAR_PREFIX + YEAR + "\\" + CameraPrefix  + "-" + Month  + Day  + "-" + batch_number)
#        C:\\users\\rogeridaho\\2022\\100-0255-04  => method for local path completion in prior versions of STT2XML
#  this path can be conveniently built from env vars and the DCIM foldername to maintain backward compatibility as well as portability   
    sourcefolder = source
    destinationfolder = destination
    os.makedirs(destinationfolder)

    PhotoFileList = []
    PhotoFileList = os.listdir(sourcefolder)
    TotalFiles = len(PhotoFileList)
    print(f'MSG: First image file: {PhotoFileList[0]}, Last Image file: {PhotoFileList[TotalFiles-1]}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
    for filename in PhotoFileList:
        localpath = sourcefolder + "\\" + filename
        destinationpath = destinationfolder + "\\" + filename
        # print(f"Source path is: {localpath}")
        # print(f"Destination path is: {destinationpath}")
        try:
            shutil.copy(localpath, destinationpath)
            pass
        except:
            print(f'MSG:  Copy image files failed.  Module: {__name__}, Line:  {inspect.getframeinfo(inspect.currentframe()).lineno}')
            sys.exit(1)
    print(f'MSG: Copied {len(PhotoFileList)-1} files numbered {PhotoFileList[0]} to {PhotoFileList[149]} from {sourcefolder} to {destinationfolder}, Module {__name__},line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
    return

def CopyPhotosToSFTP(sourcefolder, destinationfolder):
    """accepts two strings, copies image files SD to SFTP server, returns exit(0) for success, exit(1) for failure 
    """
    SFTP_SERVER = "rogeridaho.sftp.wpengine.com"
    SFTP_ACCOUNT = "rogeridaho"
    SFTP_PASSWORD = "Cyb4rS4cur1ty!!##"  # should be secured via environment variable in VM
    SFTP_PORT = 2222
    SFTP_PROTOCOL = "SFTP"
    print(f'MSG: SFTP DEST PATH:  {destinationfolder}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
    transport = paramiko.Transport((SFTP_SERVER, SFTP_PORT))
    transport.connect(username=SFTP_ACCOUNT, password=SFTP_PASSWORD)
    if transport.connect:
        print(f"MSG: SFTP Connection established, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}")
    sftp = paramiko.SFTPClient.from_transport(transport)
    UploadCounter = 0
    PhotoFileList = []
    PhotoFileList = os.listdir(sourcefolder)
    #print(f'{PhotoFileList}')
    for filename in PhotoFileList:
        localpath = sourcefolder + "\\" + filename
        destinationpath = destinationfolder + "/" + filename
        # print(f"Source path is: {localpath}")
        # print(f"Destination path is: {destinationpath}")
        # sftp.put(localpath, destinationpath)
        #print(f'MSG: Simulated Upload of: {localpath} to {destinationpath}. Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
        # print(f"File #{UploadCounter}")
        UploadCounter += 1
    print(f'MSG: {UploadCounter-1} files uploaded from {localpath} to {destinationpath}. Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
    sftp.close()
    transport.close()
    return

def ArchivePhotos(sourcefolder, ImagesFolderName, BatchNum): # call asynchronously so backup can be done while script runs.  
    ArchiveDestinationRootFolder = 'C:\\user\\roger\\BAK\\'
    MonthStub = ImagesFolderName[4:8] + '\\'
    DayStub = ImagesFolderName[8:10] + '\\'
    BatchNumStub = BatchNum + '\\'

    os.chdir(ArchiveDestinationRootFolder)
    os.mkdir(Month)
    os.chdir(Month)
    os.mkdir(Day)
    os.chdir(Day)
    os.mkdir(BatchNum)
    os.chdir(BatchNum)
    
    PhotoFileList = []
    PhotoFileList = os.listdir(sourcefolder)
    #print(f'{PhotoFileList}')
    for filename in PhotoFileList:
        localpath = sourcefolder + "\\" + filename
        ArchiveDestinationPath = ArchiveDestinationRootFolder + MonthStub + DayStub + BatchNum + filename
        print(f'MSG: Source path is: {localpath}. Modele: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
        print(f'Archive path is: {ArchiveDestinationPath}. Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
        try:
            shutil.copy(localpath, ArchiveDestinationPath)
            pass
        except:
            print(f'MSG:  Copy image files failed.  Module: {__name__}, inspect.getframeinfo(inspect.currentframe()).lineno')
            sys.exit(1)
    return