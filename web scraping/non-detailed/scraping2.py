from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		return None

	try:
		bsObj=BeautifulSoup(html.read())
		Titlecontent=bsObj.body.h1
	except AttributeError as e:
		print('tag not found')
	return Titlecontent

title=getTitle('http://localhost/BIDIIcorp/home.html')
if title == None:
	print('title not found')

else:
	print(title)