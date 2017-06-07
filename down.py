import urllib 
import os
from bs4 import BeautifulSoup as bs

cwd= os.getcwd()
print cwd
for i in range(1700,1800):
    u=urllib.urlopen('https://www.xkcd.com/'+ str(i))
    data = bs(u,"lxml")
    link= map(lambda x: x.get('src') , filter( lambda x: x.has_attr('title') ,data.find_all('img')))
    alt= map(lambda x: x.get('title') , filter( lambda x: x.has_attr('title') ,data.find_all('img')))
    img='http://www.'+link[0][2:]
    name=link[0][23:]
    urllib.urlretrieve(img,name)
    print name[:-4]
    os.mkdir(name[:-4])
    f=open(name[:-4]+'.txt','w')
    f.write(alt[0].encode('utf-8'))
    f.close()
    os.rename(cwd+'/'+name[:-4]+'.txt',cwd+'/'+name[:-4]+'/'+name[:-4]+'.txt')
    os.rename(cwd+'/'+name,cwd+'/'+name[:-4]+'/'+name)
