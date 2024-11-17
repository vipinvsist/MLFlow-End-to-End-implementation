import os
from mlflowProject import logger
from mlflowProject.entity.config_entity import  DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd
import datetime

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        self.data =pd.read_csv(r"C:\ML_Projects\MLflow_Implementation\MLFlow-End-to-End-implementation\artifacts\data_ingestion\Train-Set.csv")

    def read_data(self):
        data = self.data
        logger.info("Data has been loaded")
        logger.info(data.shape)
        return data
    def data_types(self):
        # data = DataTransformation(config=DataTransformationConfig).read_data(data)
        datatypes = self.data.dtypes
        logger.info("Data types of all features inside data \n", datatypes)
        return datatypes
    
    def data_missing(self):
        # data =DataTransformation(config=DataTransformationConfig).read_data(data)

        missing = self.data.isnull().sum()/len(self.data)
        percentage_missing = missing *100
        logger.info("Data missing \n",percentage_missing)
        return percentage_missing
    
    def feature_transformation(self):
        # data = DataTransformation(config=DataTransformationConfig).read_data(data)
        data = self.data
        data['ProductID'] = data['ProductID'].apply(lambda x: x[:2])
        data['FatContent'] = data['FatContent'].apply(lambda x: "lf" if x in ['Low Fat',"low fat", "lf"] else 'reg')
        logger.info(data['ProductID'].unique())
        logger.info(data['FatContent'].unique())
        data['OutletID'] = data['OutletID'].str.replace('OUT0',"").astype(int)
        current_year = datetime.date.today().year
        data['EstablishmentYear'] = current_year - data['EstablishmentYear']
        avg_weight = data.groupby('ProductType')['Weight'].transform('mean')
        data['Weight'] = data['Weight'].fillna(avg_weight)
        data_os0= data[data['OutletSize'].isnull()]
        data_os1 = data[~data['OutletSize'].isnull()]
        data_os0.loc[:,'OutletSize'] = data_os0.loc[:,'LocationType'].apply(lambda x:'Medium' if x =="Tear3" else 'Small')
        data = pd.concat((data_os0,data_os1),axis='rows')
        # X =data.drop("OutletSales",axis='columns')
        # y = data['OutletSales']
        logger.info(data.shape)
        # logger.info(X.shape)
        # logger.info(y.shape)
        return data                                 #, X, y
    def data_split(self):
        data = self.feature_transformation()
        train,test = train_test_split(data,test_size=0.1,random_state=42)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index =False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        print(test.shape)
        print(train.shape)
