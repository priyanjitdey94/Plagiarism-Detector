# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:22:39 2016

@author: Priyanjit Dey
"""
import difflib
import sys
from os import listdir,path
from os.path import isfile,join

'''
@getFileInfo:
  Method responsible for converting the source code in a single string for better testing
  1. All whitespaces, newlines, tabs are removed
  2. Single and multi line comments are ignored
  3. Header files not considered in C/C++
  4. Preprocessor directives and macros not considered.
'''
def getFileInfo(fname):
    f=open(fname)
    f_line=f.readline();
    s=""
    while f_line!='':
        f_line=f_line.replace(" ","")
        f_line=f_line.replace("\t","")
        f_line=f_line.replace("\n","")
        f_line=f_line.replace("\r","")
        
        #Removing preprocessor, macros and headers
        if f_line!='' and f_line[0]=='#':
            f_line=f.readline()
            continue
        #Removing single line comments
        elif f_line!='' and f_line[0]=='/' and f_line[1]=='/':
            f_line=f.readline()
            continue
        #Removing multiline comments
        elif f_line!='' and f_line[0]=='/' and f_line[1]=='*':
            while f_line[len(f_line)-1]!='/' and f_line[len(f_line)-2]!='*' and f_line!='':
                f_line=f.readline()
                f_line=f_line.replace(" ","")
                f_line=f_line.replace("\t","")
                f_line=f_line.replace("\n","")
                f_line=f_line.replace("\r","")     
        #No other condition
        else:
            s=s+f_line
        
        f_line=f.readline()
    
    f.close()    
    return s




try:
    pathName=raw_input("Please enter a valid path: ")
except IOError as e:
    print "Something wrong with the path. Please check."
    sys.exit()

listOfFiles=[f for f in listdir(pathName) if(isfile(join(pathName,f) ) )]

#print listOfFiles[1]
print "The list of files present in this directory: "
print '\n'.join(listOfFiles)

print "\n\nResult(Any two files having greater than 40% similarity will be reported):"

pathName=pathName+"\\"
basePath=path.dirname(pathName)

cheatFile1=[]
cheatFile2=[]
cheatPercentage=[]

for i in range(0,len(listOfFiles)):
    filePath1=path.abspath(path.join(basePath,listOfFiles[i]))
    s1=getFileInfo(filePath1)
    for j in range(i,len(listOfFiles)):
        if i==j:
            continue
        filePath2=path.abspath(path.join(basePath,listOfFiles[j]))
        s2=getFileInfo(filePath2)
        match=max(difflib.SequenceMatcher(None,s1,s2),difflib.SequenceMatcher(None,s2,s1))        
        if match.ratio()*100>=40.00:
            cheatFile1.append(listOfFiles[i])
            cheatFile2.append(listOfFiles[j])
            cheatPercentage.append(str(match.ratio()*100))
        #print(listOfFiles[i]+" "+listOfFiles[j]+" ")
        #print(match.ratio()*100)


if not cheatFile1:
    print "Looks like no one cheated!"
else:
    for i in range(len(cheatPercentage)):
        print(str(i+1)+". "+cheatFile1[i]+" "+cheatFile2[i]+" "+cheatPercentage[i])

