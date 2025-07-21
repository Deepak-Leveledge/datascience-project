from src.datascience.pipelines.data_evaluation import ModelEvaluationPipeline
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.pipelines.model_training import ModelTrainerPipeline
from src.datascience import logger
from src.datascience.pipelines.data_injection import DataIngestionTrainingPipeline
from src.datascience.pipelines.data_validation import DataValidationTrainingPipeline
from src.datascience.pipelines.data_transformation import DatatransformationTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DatatransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    config = ConfigurationManager()
    model_trainer_config = config.get_model_trainer_config()
    obj = ModelTrainerPipeline(config=model_trainer_config)
    obj.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
# logger.info("Logging has been set up successfully.")






STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_evaluation_pipeline = ModelEvaluationPipeline(config=ConfigurationManager().get_model_evaluation_config())
    data_evaluation_pipeline.initiate_model_evaluation()
    
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e