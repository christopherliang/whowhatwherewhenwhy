import urllib2
from bs4 import BeautifulSoup

url="http://names.mongabay.com/baby-names/application/top-F-US-2011.html"

request = urllib2.urlopen(url)
result = request.read()
soup = BeautifulSoup(result, 'html.parser')

print soup
