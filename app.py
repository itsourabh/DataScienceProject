import sys

from src.DataScienceProject.components.data_ingestion import DataIngestion
from src.DataScienceProject.components.data_ingestion import DataIngestionConfig
from src.DataScienceProject.exception import CustomException
from src.DataScienceProject.logger import logging

if __name__=="__main__":
    logging.info("The execution has started")
    
    
    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        raise CustomException(e,sys)