# !/usr/bin/python

import traceback
import pandas as pd

"""
Created on July 10
@author Jugal
"""
class FileLoader:
    "Loads hdfs files"
    
    def __init__(self):
        pass
    
    """
    Loads Files
    @param spark sparksession
    @param format_ fileformat
    @param flag boolean
    @param path targetpath
    @param log logger
    @return dataframes
    """
    def __load_csv_files(self,path,sep,log):
        try:
            return pd.read_csv(path,sep,skipinitialspace=True)
        except Exception as e:
            log.error("FileLoader,__load_files, exception",traceback.print_exc())
            
    
    def __load_json_files(self,path,log):
        try:
            print(path)
            return pd.read_json(path,lines=True)
        except Exception as e:
            log.error("FileLoader,__load_files, exception",traceback.print_exc())        