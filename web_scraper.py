import urllib2
import google
import re
from bs4 import BeautifulSoup


def searchURL(urls, ix, file):
	try:
		print(ix)
		page = urllib2.urlopen(searches[ix]).read()
		soup = BeautifulSoup(page, "html.parser")
		soup.prettify()
		for anch in soup.findAll('a', href = True):
			printToFile(file, ix, anch)
		ix += 1

		if(ix >= len(urls)):
			return True
		else:
			searchURL(urls, ix, file)
	except:
		ix += 1
		if(ix >= len(urls)):
			return True
		else:
			searchURL(urls, ix, file)

def printToFile(file, ix, object):
	file.write(object['href'])
	file.write("{})\n\n".format(ix))


search_val = raw_input("Enter what you want to search for: ").lower()
print(search_val)

#search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
searches = []
for url in google.search(search_val, stop = 10):
	searches.append(url)

for x in searches:
	print(x)

text_file = open("search_results.txt", "w")
searchURL(searches, 0, text_file)

text_file.close()




