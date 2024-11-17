from src.mlflowProject import logger
from src.mlflowProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlflowProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlflowProject.pipeline.satge_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} COMPLETED <<<<<<<< \n \nx========x")
except Exception as e :
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"
try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<<<\n \nx=======")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"

try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<<<\n \nx=======")
except Exception as e:
        logger.exception(e)
        raise e