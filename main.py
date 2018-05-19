from urllib.request import Request, urlopen, URLError, HTTPError
import urllib.error
import datetime

import time


def header():
	print("""
___  ___  ___  ______ 
|  \/  | / _ \ |  ___|
| .  . |/ /_\ \| |_   
| |\/| ||  _  ||  _|  
| |  | || | | || |    
\_|  |_/\_| |_/\_|
MULTIPLE ADMIN PANEL FINDER
                   --Made By :: B!@CKC0Br4 & PRATEEK
                   -- GRETZ TO ALL MEMBER OF ICH
___________________________________________________              
""")


def getfilename(path):
	slashcounter = 0
	pos = 0
	for char in path:
		if char is '/':
			slashcounter += 1
#print(path[pos])
	while (slashcounter != 0):
		if (path[pos] == '/'):
			slashcounter -= 1
		pos += 1
	name = path[pos:]
	return name


def formaturl(checkwebsite, addpath):
	if not checkwebsite.startswith("http"):
		checkwebsite = "http://" + checkwebsite
	finalweblink = checkwebsite + addpath
	return finalweblink


header()
#time.sleep(2.5)
path = str(input("Enter Path of website list :: "))
web_fname = getfilename(path)
#File name is present in web_fname
webfile = open(web_fname, "r")
websitelist = webfile.read().splitlines()
path = open("path.txt", "r")
pathlist = path.read().splitlines()
weblist=[]
for website in websitelist:
	num = 1
	print("_____________{}_________________".format(website))
	for path in pathlist:
		link = formaturl(website, path)
		req = Request(link)
		try:
		  response = urlopen(req)
		except HTTPError as e:
		  print('\033[1;31m[-]\033[1;m %s'% link)
		except URLError as e:
		  print('\033[1;31m[-]\033[1;m %s'% link)
		else:
		  print ('\033[1;32m[+] %s'% link)
		  weblist.append(link+"\n")
weblistfile=open("adminpathlistof::"+web_fname,"w")
n=len(weblist)
for i in range(n):
	website=str(weblist[i])
	weblistfile.write(website)
print("\n\n Everyhing completed successfully ..\n")
print ('\033[1;32m[+] List of Admin panel path is saved with file name :- adminpathlistof:: %s'% web_fname)

