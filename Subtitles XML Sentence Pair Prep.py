
# coding: utf-8

# In[ ]:

from xml.dom import minidom
xmldoc = minidom.parse("moviefile.xml")
document = xmldoc.getElementsByTagName("document")[0]
s = document.getElementsByTagName("s")

meta = document.getElementsByTagName("meta")[0]
source = meta.getElementsByTagName("source")[0]
genre = source.getElementsByTagName("genre")[0]
genres = (genre.firstChild.data)

genrelist = ["Comedy", "Drama" ,"Romance"]
for genre in genrelist:
    if genre in genres:
        print ("accept movie")
        break
        
sentence = []
for i in s:
    w = i.getElementsByTagName("w")
    words = []
    for i in w:
        words.append(i.firstChild.data) 
    sentence.append(' '.join(words))
    
datapairs = []
for i in range (0,len(sentence)-1):
    datapairs.append(sentence[i])
    datapairs.append(sentence[i+1])

