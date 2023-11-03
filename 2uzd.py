""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.
1)RSS? Jaunumi un saturs; satura agregators - sistēma, kas ļauj abonēt interesējošos avotus
2)plūsmu no google.lv
"""
import feedparser

# URL uz RSS plūsmu
rss_url='https://www.lsm.lv/laika-zinas/:lv'

# iegūstam RSS plūsmas datus un veicam analīzi
kkk=feedparser.parse(rss_url)

# noformēšana...
for entry in kkk.entries:
    print("Virsraksts", entry.title)
    print("Saite:", entry.link)
    print("Publicēšanas datums", entry.published)
    print("\n")