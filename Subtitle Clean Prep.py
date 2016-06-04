
# coding: utf-8

# In[4]:

Text = []
for line in open('sub1.srt'):
    if not line[0].isdigit():
        if line != "\n":
            cleanline = line.strip('\n').replace("</i>","").replace("<i>","").replace("\t"," ")
            Text.append(cleanline)
            
for x in range (0,10):
    newfilelengthcount = len(Text)
    lentext = len(Text)
    i = 0
    while i < newfilelengthcount-1:
        if Text[i][-3:-1] == "..":
            if i +1 != lentext:
                Text[i] = Text[i] + " " + Text[i+1]
                del Text[i+1]
            i = i + 1
            newfilelengthcount = newfilelengthcount-1
        elif Text[i][-1] not in [".","?","!","-"]:
            if i +1 != lentext:            
                Text[i] = Text[i] + " " + Text[i+1]
                del Text[i+1]
            i = i + 1
            newfilelengthcount = newfilelengthcount-1
        else:
            i = i + 1

exclude = set("/ï»¿1#0<>=â™ªÃ©")
for i in range (0,len(Text)):
    Text[i] = Text[i].replace("- "," ").replace("--"," ").replace("...","")
    Text[i] = ''.join(ch for ch in Text[i] if ch not in exclude)
for i in range (0,len(Text)):
    Text[i].replace("\\","")

