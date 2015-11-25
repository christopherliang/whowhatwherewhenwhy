"""
import urllib2
from bs4 import BeautifulSoup

url= "https://www.google.com/search?client=ubuntu&channel=fs&q=http+error+403&ie=utf-8&oe=utf-8#channel=fs&q=http+error+403+beautifulsoup"
hdr = {'User-Agent': 'Mozilla/5.0'}
request = urllib2.Request(url,headers=hdr)
result = request.read()
soup = BeautifulSoup(result, 'html.parser')

print soup
"""

import urllib2, sys, re
from bs4 import BeautifulSoup

site= "http://names.mongabay.com/baby-names/application/top-F-US-2011.html"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
raw = soup.get_text()
text = re.sub("[\t\n ]"," ",raw)

exp = "[A-Z][a-z]+"

result = re.findall(exp,text)
print result
