import os
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path
from mlflowProject.entity.config_entity import ModeEvaluationConfig
from mlflowProject.utils.common import save_json
import dagshub

class ModeEvaluation:
    def __init__(self,config :ModeEvaluationConfig):
        self.config = config

    def eval_metrices(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)

        return rmse, mae, r2
      
    def log_into_mlflow(self):
        dagshub.init(repo_owner='vipinvsist', repo_name='MLFlow-End-to-End-implementation', mlflow=True)
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        test_x=pd.get_dummies(test_x)
        test_y=np.log(test_y)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        dagshub.init(repo_owner='vipinvsist', repo_name='MLFlow-End-to-End-implementation', mlflow=True)

        
        
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            (rmse,mae,r2) = self.eval_metrices(test_y,predicted_qualities)

            # saving the loaded  metrices

            scores = {"rmse": rmse, "mae" : mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name),data =scores)

            for key, value in self.config.all_params.items():
                mlflow.log_param(key, value)

            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("r2",r2)
            mlflow.log_metric("mae",mae)


            if tracking_url_type_store !='file' :
                # Register the model
                # There are other ways also , follow below link tknow more:
                # https://mlflow.org/docs/latest/model-registery.html#api-workflow
                model_uri = mlflow.sklearn.log_model(model, "model")  
            # else:
            #     model_uri = mlflow.sklearn.load_model(model, "model")