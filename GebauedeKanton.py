# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:33:18 2021

@author: marce
"""

#https://docs.python.org/3/library/re.html#module-re

import os
import pandas as pd

os.chdir("C:/Users/marce/Downloads")
data = pd.read_csv("px-x-0902010000_103_20210403-133126.csv", sep=";",header=None,skiprows=1,names=['Hierarchie','Gebaeude','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])

#exclude all rows grösser Hierarchie Gemeinde, also jende die nicht "..." entahlten

data = data[data.Hierarchie.str.match("\.")]

#neues Attribut Gemeinde (Vollständiger Name noch pending und ä,ü,ö fehlend)
data['Gemeinde']=data['Hierarchie'].str.extract('([A-Z]\w{0,})', expand=True)

#neues Attribut Gemeinde 
data['PLZ']=data['Hierarchie'].str.extract('([0-9]\w{0,})', expand=True)

# Print the header info of data (first five rows)
data.head(5)

