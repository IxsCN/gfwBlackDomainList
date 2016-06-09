#!/usr/bin/env python  
#   Aug 19 2011  
#   Copyleft@2011 Published Under BSD Lisense  
#           Ronald Liu  
#   lzsdc01@gmail.com  
#   FYI  http://lzsblog.appspot.com/%3Fp%3D291001  
#     
 
#   Mod By D2o 2012/8/13  
#   http://conupefox.csdn.net  
 
#   Mod By DeadWood 2014/7/7  
#   http://www.xiumu.org  
 
import sys,re,base64,cStringIO,urllib2  
 
def splitList(txt):  
    arr = txt.split("\n")  
    pattern ='^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$'  
    l = []  
    for line in arr:  
        if (not len(line)): #empty line  
            continue  
        if (line[0] == "!"): #Comment line  
            continue  
        elif(line[0:2] =="@@"):#Forbidding line  
            continue  
        elif(line.find("/")!=-1 or line.find("*")!=-1 or line.find("[")!=-1 or line.find("%")!=-1 or line.find(".")==-1 ): #URL is ignored, only domains left  
            continue  
        elif(re.search(pattern, line)):#IP address  
            continue  
 
        #In this case, domain name is irrelevant to protocol(http or https)  
        elif(line[0:2] =="||"):  
            l.append(line[2:])  
        elif(line[0] == "."):  
            l.append(line[1:])  
        else:  
            l.append(line)  
 
    return l  
 
 
#Decode and decorate the input string  
url = urllib2.urlopen('https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt',timeout=10) 
f = cStringIO.StringIO(url.read()) 
txt = f.read()  
txt = base64.decodestring(txt)  
domains = splitList(txt)  
fh=open("gfwlist.list","wb+")
per_line=""  
print "#gfwlist"
for line in domains:  
    if (line!=per_line):  
       print line 
       fh.write(line+"\n")
    per_line=line
fh.close()
