# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 22:52:12 2017

@author: Akshay
"""

import os
os.chdir("C:\\Users\\Akshay\\Dropbox\\Personal\\Data Science\\iPython\\Personal\\Practice")
os.getcwd()
document  = open("test_document.txt", "r")
x = document.read()
xl = x.split()
xl

#Problem statement - #Wearethepeople\nHimynameisakshay\npythonisfun\nwithouthim\nsuperman\ndestabilize\n

dict1 = ['We','are','the','people','Hi','my','name','is','akshay','python','without','him','fun','superman','super','man','superman','stabilize','destabilize']
dict1

biglist=[]
for i in xl:
    h=0
    templist=[]
    g=0
    for j in range(len(i)):
        element = i[g:j+1]
        if element in dict1:
            g = j+1
            templist.append(element)
    biglist.append(templist)


a=[1,2,3,4]
[x**2 for x in a]

