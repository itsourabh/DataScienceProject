import os
import sys

import numpy as np
import pandas as pd
import pymysql
from dotenv import load_dotenv

from src.DataScienceProject.exception import CustomException
from src.DataScienceProject.logger import logging

load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
passw=os.getenv("password")
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading mysql database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=passw,
            db=db
        )
        logging.info("Connection Establish",mydb)
        df=pd.read_sql_query('select * from student',mydb)
        print(df.head())
        
        return df
    
    
    except Exception as ex:
        raise CustomException(ex)