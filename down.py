#### Stores images into a separate folder with alt-text in a text file

import urllib
import os
from bs4 import BeautifulSoup as bs

cwd = os.getcwd()
print "Will be saved in " + cwd
k, j = map(int, raw_input("Enter range ").split())
for i in range(k,j+1):
    u = urllib.urlopen('https://www.xkcd.com/' + str(i))
    data = bs(u, "lxml")
    ImageContainer = filter(lambda x: x.has_attr('title'), data.find_all('img'))
    link = map(lambda x: x.get('src'), ImageContainer)
    if not link:
        print "Comic #" + str(i) + " doesn't exist"
        continue
    alt = map(lambda x: x.get('title'), ImageContainer)
    img = 'http://www.' + link[0][2:]
    name = link[0][23:]
    urllib.urlretrieve(img, name)
    print name[:-4]
    os.mkdir(name[:-4])                        ### comment this and the lines below if you don't
    f = open(name[:-4] + '.txt', 'w')          ### want it in a seperate folder and don't want 
    f.write(alt[0].encode('utf-8'))            ### the alt-text
    f.close()
    os.rename(cwd + '/' + name[:-4] + '.txt', cwd + '/' + name[:-4] + '/' + name[:-4] + '.txt')
    os.rename(cwd + '/' + name, cwd + '/' + name[:-4] + '/'+name)
