from mlflowProject.config.configuration import ConfigurationManager
from mlflowProject.components.model_evalution import ModeEvaluation
from mlflowProject import logger

STAGE_NAME = "Model Eval stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModeEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n \nx================x")

    except Exception as e:
        logger.exception(e)
        raise e