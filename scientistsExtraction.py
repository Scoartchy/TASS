#ctrl + B to run
import bs4 as bs
import urllib.request
import time
import numpy as np

siteSourceCodeAE = urllib.request.urlopen('https://scholar.google.com/citations?user=j2MGGBAAAAAJ&hl=en').read()
#siteSourceCodeAE = urllib.request.urlopen('https://scholar.google.pl/citations?user=qc6CJjYAAAAJ&hl=pl&oi=ao').read()

soup = bs.BeautifulSoup(siteSourceCodeAE, 'lxml')

#print(siteSourceCodeAE)
#print(soup)

for these in soup.find_all('a', class_='gsc_a_at') : 
	print(these, '\n')
	#print(these, '\n https://scholar.google.pl', these.get('data-href'), '\n')
	#time.sleep((30-5)*np.random.random()+5) #from 5 to 30 seconds
	#siteSourceCode = urllib.request.urlopen('https://scholar.google.pl' + these.get('data-href'))
	#print(siteSourceCode)
	#soup2 = bs.BeautifulSoup(startingSiteSourceCode, 'lxml')
	


