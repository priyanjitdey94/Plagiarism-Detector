# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:22:39 2016

@author: Priyanjit Dey
"""
import difflib

def getFileInfo(fname):
    #fname=input("File Name:")
    f=open(fname)
    f_line=f.readline();
    s=""
    while f_line!='':
        f_line=f_line.replace(" ","")
        f_line=f_line.replace("\t","")
        f_line=f_line.replace("\n","")
        f_line=f_line.replace("\r","")
        if f_line!='' and f_line[0]=='#':
            f_line=f.readline()
            continue
        elif f_line!='' and f_line[0]=='/' and f_line[1]=='/':
            f_line=f.readline()
            continue
        elif f_line!='' and f_line[0]=='/' and f_line[1]=='*':
            while f_line[len(f_line)-1]!='/' and f_line[len(f_line)-2]!='*' and f_line!='':
                f_line=f.readline()
                f_line=f_line.replace(" ","")
                f_line=f_line.replace("\t","")
                f_line=f_line.replace("\n","")
                f_line=f_line.replace("\r","")     
            #s=s+f_line                           
        else:
            s=s+f_line
        f_line=f.readline()
    f.close()    
    return s



fname1 = raw_input("Enter the first filename: ")
s1=getFileInfo(fname1)
fname2 = raw_input("Enter the second filename: ")
s2=getFileInfo(fname2)
print(s1+'\n')
print(s2+'\n')
match=difflib.SequenceMatcher(None,s1,s2)
print(match.ratio()*100)    
