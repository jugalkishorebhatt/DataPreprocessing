# !/usr/bin/python

import pyspark
from pyspark.sql import SparkSession
import traceback


"""

"""
class SparkConfig:
    "Initializes Spark Config"
    
    def __init__(self):
        pass
        
    """
    Initializes SparkSession
    @param log logger
    @return sparkSession
    """    
    def __init_spark(self, log):
        try:
            return SparkSession.builder.appName("DataProcessing").getOrCreate()
        except Exception as e:
            log.error("SparkConfig, __init_spark", traceback.print_exc())    
