#!/usr/bin/>env python2
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup


categories = {
"PC": "http://www.jeuxvideo.com/pc.htm", 
"PS3": "http://www.jeuxvideo.com/ps3-playstation-3.htm",
"360": "http://www.jeuxvideo.com/x360-xbox-360.htm",
"WII U": "http://www.jeuxvideo.com/wii-u-nintendo-wii-wiiu.htm",
"WII": "http://www.jeuxvideo.com/wii-nintendo-wii.htm",
"3DS": "http://www.jeuxvideo.com/3ds-nintendo-3ds.htm",
"VITA": "http://www.jeuxvideo.com/ps-vita-playstation-vita.htm",
"DS": "http://www.jeuxvideo.com/ds.htm",
"IPHONE": "http://www.jeuxvideo.com/apple-iphone-ipod-touch.htm",
"ANDROID": "http://www.jeuxvideo.com/android.htm",
"WEB": "http://www.jeuxvideo.com/actualite-jeux-en-ligne.htm"}

for keys in categories:
    print keys, 
print
print
choix_categorie = raw_input("Choisissez parmi les catégories ci-dessus : ")

while not categories.has_key(choix_categorie):
    print "Catégorie non-existante !"
    choix_categorie = raw_input("Choisissez parmi les catégories ci-dessus : ")



print "Chargement des news..."

f = urllib2.urlopen(categories[choix_categorie])
soup = BeautifulSoup(f)
f.close()


liste_ul = soup.findAll("ul", attrs={"class": "liste_liens"})

liste_news = []

for ul in liste_ul:
    for li in ul.findAll("li"):
        for a in li.findAll("a"):
            if "news" in str(a):
                if len(a.attrs) > 1:
                    title = a["title"]
                    liste_news.append((" "+title,a["href"]))
                else:
                    liste_news.append((a.string,a["href"]))

print "News: " 
for news, link in liste_news:
    print "- %s (%s)" % (news, link)
