# !/usr/bin/python

import traceback
import pandas as pd

"""
Created on December 06
@author Jugal
"""
class DataConvert:
    "Creates Dataframe for the fixed Length File"
    
    
    "Initializer"
    def __init__(self,data):
        self.data = data
    
        
    #------------Describes about each Field-----------
    def __describeData(self,value):
        print(value.describe())

    #------------Checks for any empty values and gives a count---
    def __checkEmpty(self,value):
        print(value.isnull().sum())

    #-----------List the values in a field------------
    def __checkTypo(self,value):
        sort = value.value_counts()
        print(sort.sort_index())

    #----------Removes Extra spaces from the field
    def __stripSpace(self,value):
        return self.data[value].str.strip()
    
    #---------Converts all the values to lower case------
    def __convStrLow(self,value):
        return self.data[value].str.lower()

    #---------Replaces Typo's in the field
    def __replaceString(self,value,old,new):
        return self.data[value].replace(old,new,inplace=True)

    #---------List the values in in the field which is null
    def __filterData(self,value):
        print(self.data.loc[value.isnull(),:])
        
    #----------Convert Categorical Data to categories type
    def __convCategories(self,value):
        return self.data[value].astype('category')
    
    def __fillNa(self,value,groups,transforms):
        return self.data[value].fillna(self.data.groupby(groups)[value].transform(transforms), inplace=True)
    