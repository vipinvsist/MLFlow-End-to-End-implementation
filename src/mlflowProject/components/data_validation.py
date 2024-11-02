import os
import pandas as pd
from mlflowProject import logger
from mlflowProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self)-> bool:
        try:
            validation_stauts = None

            data = pd.read_csv(self.config.unzip_data_dir)
            data['Weight'].fillna(data['Weight'].mean(),inplace=True)
            data['OutletSize'].fillna(data['OutletSize'].mode()[0],inplace=True)
            data.drop(["ProductID", "OutletID"], axis=1, inplace=True)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_stauts = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_stauts}")
                else: 
                    validation_stauts = True
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"validation status: {validation_stauts}")
            return validation_stauts
        except Exception as e:
            raise e

