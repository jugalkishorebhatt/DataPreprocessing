# !/usr/bin/python

import pandas as pd
import numpy as np

import logging
import yaml

from common import FileLoader
from common import DataViz
from common import SupervisedLearning
from action import DataConvert



"""
Created on December 06
@author Jugal
"""
class AppDataPreprocessing:
    
    def __init__(self):
        pass
        
if __name__ == "__main__":
    "This Object creates the App Class"
    
    logging.basicConfig(filename = './logname.log', 
                            filemode = 'a', 
                            format = '[[%(filename)s:%(lineno)s :] %(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s', 
                            datefmt = '%H:%M:%S', 
                            level = logging.DEBUG)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logger.info('Data Preprocessing')
    
    try:
        with open('C:\\Users\\DataProcessing\\main\\config.yml', 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
    except Exception as e:
        logger.error("Main Method, config file", traceback.print_exc())
        
           
    # Needs to be made configurable
    data = pd.read_csv("C:\\Users\\Automobile.csv",sep="#",header=None,names=['symboling','normalized-losses','make','fuel_type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price'],skipinitialspace=True)
    data.drop_duplicates(keep='first',inplace=True)
    print(data)

    # List of categorical data
    categorical_list = ['make', 'fuel_type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'fuel-system','engine-type','num-of-cylinders']
     
    #----------Sanity Check----------
    for i in categorical_list:
        print("-----------")
        print("Column Name: ",i)
        data[i] = DataConvert.DataConvert(data)._DataConvert__stripSpace(i)
        print("-----------")
        data[i] = DataConvert.DataConvert(data)._DataConvert__convStrLow(i)
        print("------Checking for Empty-----")
        DataConvert.DataConvert(data)._DataConvert__checkEmpty(data[i])
        print("----Check for Typo's-------")
        DataConvert.DataConvert(data)._DataConvert__checkTypo(data[i])
        print("-----Describe Data------")
        data[i] = DataConvert.DataConvert(data)._DataConvert__convCategories(i)
        print("-----Describe Data------")
        DataConvert.DataConvert(data)._DataConvert__describeData(data[i])
        print("************")
        
    # List of Measuring data
    measurement_list = ['symboling','normalized-losses','wheel-base','engine-size','wheel-base', 'length', 'width', 'height', 'curb-weight','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']
    
    #----------Sanity Check----------
    for i in measurement_list:
        print("-----------")
        print("Column Name: ",i)
        print("------Checking for Empty-----")
        DataConvert.DataConvert(data)._DataConvert__checkEmpty(data[i])
        print("-----Describe Data------")
        DataConvert.DataConvert(data)._DataConvert__describeData(data[i])
        print("-----Filter Empty Data------------")
        DataConvert.DataConvert(data)._DataConvert__filterData(data[i])
        print("************")
    
    
    data["price"].fillna(data.groupby(["make"])["price"].transform("median").round(1), inplace=True)
    #---------Replace Typo Values--------
    replace = FileLoader.FileLoader()._FileLoader__load_json_files(cfg['schema']['replaceQual'],logger)
    print(replace)
     
    for index, row in replace.iterrows():
        DataConvert.DataConvert(data)._DataConvert__replaceString(row['Column'],row['old'],row['new'])
    data['price'] = DataConvert.DataConvert(data)._DataConvert__replaceString('price',0.0,np.nan)

    #---------------Filling Data Cells-----------------

    #----------------Filling the missing values for the cells from the same set of data to get more accuracy
    Cont = FileLoader.FileLoader()._FileLoader__load_json_files(cfg['schema']['replaceQuan'],logger)
    print(Cont)
    
    
    for index, row in Cont.iterrows():
        DataConvert.DataConvert(data)._DataConvert__fillNa(row['Column'],row['groups'],row['transform'])

    #------------ Takes in the value of previous
    data["num-of-doors"].fillna(method = "ffill",inplace=True)

    #----------- Finds a linear equally and fills in the values. Which tends to be positively skewed
    data["normalized-losses"].interpolate(inplace=True)

    #----------- Assumption by understanding the data from by comparing it with other fields
    data["normalized-losses"].fillna(value=99,inplace=True)
         
    DataViz.DataViz(data)._DataViz__scatterMatrix()
