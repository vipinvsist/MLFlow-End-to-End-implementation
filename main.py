from src.mlflowProject import logger
from src.mlflowProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} COMPLETED <<<<<<<< \n \nx========x")
except Exception as e :
    logger.exception(e)
    raise e

