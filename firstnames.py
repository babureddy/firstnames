import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url="https://www.familyeducation.com/baby-names/browse-names/first-name/LETTER?page="
letters='ABCDEFGHIJKLMNOPQRSTUVWWXYZ'
for letter in letters:
	try:
		url1 = url.replace('LETTER',letter.swapcase())
		print (url1)
	except Exception as e:
		print (e)
		continue
	for i in range(1,100):
		try:
			html = urllib.request.urlopen(url1+str(i), context=ctx).read()			
		except:
			break
		firstNames=[]
		bs=BeautifulSoup(html, "lxml")
		a = bs.find_all('a')

		for x in a:
			if len(x.text)>1 and x.text[0] == letter:
				#print(x.text)
				firstNames +=[x.text]
		f=open('firstnames.txt','a')
		f.write('\n'.join(firstNames))
		f.close()