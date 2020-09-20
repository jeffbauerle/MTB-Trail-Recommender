import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(source)

print(soup)