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
class AppModelPrediction:
    
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
    data = FileLoader.FileLoader()._FileLoader__load_csv_files(cfg['dataset']['file'],cfg['dataset']['sep'],logger)
    data.drop_duplicates(keep='first',inplace=True)
    print(data)

    schema = FileLoader.FileLoader()._FileLoader__load_json_files(cfg['schema']['file'],logger)
    print(schema)
    
    categorical_list = schema[schema['flag']==1]['Column'].tolist()
    print(categorical_list)
        
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
    
    measurement_list = schema[schema['flag']==2]['Column'].tolist()
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
    
          
    #DataViz.DataViz(data)._DataViz__scatterMatrix()
    SupervisedLearning.SupervisedLearning(data)._SupervisedLearning__TrainTestData()