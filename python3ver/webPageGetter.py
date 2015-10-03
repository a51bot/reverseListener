#/user/bin/python3
#webPageGetter.py

import urllib.request
import sys


def getWebPage(site):
		if "http://" in site:
			page = urllib.request.urlopen(site)
			html = page.read()
			return html
		else:
			page = urllib.request.urlopen("http://"+site)
			html = page.read()
			return html
def main():
	if len(sys.argv) >= 2:
		try:
			if sys.argv[2] == "-f":
				if len(sys.argv[3]) >= 1:
					fout = open(sys.argv[3],'wb')
					html = getWebPage(sys.argv[1])
					fout.write(html)

		except IndexError:
				print(getWebPage(sys.argv[1]))
	else:
		print("Usage: webPageGetter.py www.google.com \n \t -f <filename>")
if __name__=="__main__":
	main()

