import os
import urllib.request as request
from pathlib import Path
from mlflowProject.entity.config_entity import (DataIngestionConfig)
import zipfile
from mlflowProject import logger
from mlflowProject.utils.common import get_size
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
    
    def extract_zip_file(self):
        """
        zip_file_path:str
        Extracts the zip file path
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
    