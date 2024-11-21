import pandas as pd
import numpy as np
import os
from mlflowProject import logger
from sklearn.linear_model import Lasso
import joblib
from mlflowProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]
        train_x=pd.get_dummies(train_data)
        train_y=np.log(train_y)

        model1 = Lasso(alpha=self.config.alpha,random_state=42,max_iter=1000,tol=0.1)
        model1.fit(train_x, train_y)

        joblib.dump(model1, os.path.join(self.config.root_dir, self.config.model_name))