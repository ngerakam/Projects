from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def myUrl(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		print('the url was not found')
	else:
		bsObject=BeautifulSoup(html.read())
	finally:
		print('see results')
	return bsObject
	

myurl=myUrl("http://localhost/BIDIIcorp/home.html")
if myurl==None:
	print('url not found')
else:
	print(myurl)
