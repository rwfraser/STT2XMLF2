"""MEDGlobals stores global CONSTANTS
"""
# Code upgrade: place this config data in a global application object.  

import os
import inspect
from datetime import date
from inspect import getframeinfo, currentframe

DEPLOYMENT = ''
DEFAULT_USER = ''
try:
	DEPLOYMENT = os.environ["DEPLOYMENT"].strip()
except: # no DEPLOYMENT environment variable
	pass
DEFAULT_USER_QUOTED =  os.environ['USERNAME']
DEFAULT_USER = DEFAULT_USER_QUOTED[1:-1]
YEAR_OBJ = date.today()
YEAR_STR = str(YEAR_OBJ)
YEAR = YEAR_STR[0:4]
DEFAULT_BATCH_SIZE = 150
DEFAULT_PHOTOS_PER_ITEM = 5
DefaultSourceFolder = "DCIM"
DefaultLocalDrive = "C:"

if DEPLOYMENT == "'DEVELOPMENT'":
	# Global Variables set for Development environment
	DefaultLogicalDrive = "G:"
elif DEPLOYMENT == "'PRODUCTION'":
	DefaultLogicalDrive = "G:"
else:
	DEFAULT_USER = DEFAULT_USER_QUOTED
	DefaultLogicalDrive = "G:"

# print(f'MSG: DEPLOYMENT setup is: {DEPLOYMENT}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')
print(f'MSG: DEFAULT_USER is: {DEFAULT_USER}, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno}')

