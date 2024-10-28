import os
import urllib.request as request
from pathlib import Path
from src.mlflowProject.entity.config_entity import (DataIngestionConfig)
import zipfile
from src.mlflowProject import logger
from src.mlflowProject.utils.common import get_size
import urllib.error

class DataIngestion :
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )

            logger.info(f"{filename} downloaded! with following info: \n{headers}")

        else:
            logger.info(f"File already exist of size: {get_size(self.config.local_data_file)}")

    # def download_file(self):
    #     if not os.path.exists(self.config.local_data_file):
    #         logger.info(f"Attempting to download from {self.config.source_URL}")
    #         try:
    #             filename, headers = request.urlretrieve(
    #                 url=self.config.source_URL,
    #                 filename=self.config.local_data_file
    #             )
    #             logger.info(f"{filename} downloaded! with the following info: \n{headers}")
    #         except urllib.error.HTTPError as e:
    #             logger.error(f"Failed to download file from {self.config.source_URL}: {e}")
    #         except Exception as e:
    #             logger.error(f"An error occurred: {e}")
    #     else:
    #         logger.info(f"File already exists of size: {get_size(self.config.local_data_file)}")

    
    def extract_zip_file(self):
        """
        zip_file_path:str
        Extracts the zip file path
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
    