
from src.datascience.pipelines.data_transformation import DatatransformationTrainingPipeline
from src.datascience.components.data_traning import ModelTrainer
from src.datascience.entity.config_entity import DataModelTrainingConfig
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation,DataValidationConfig
from src.datascience import logger


STAGE_NAME = "Model Trainer Stage"


class ModelTrainerPipeline:
    def __init__(self, config: DataModelTrainingConfig):
        self.config = config

    def initiate_model_training(self):
        try:
            model_trainer = ModelTrainer(config=self.config)
            model_trainer.train()
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == "__main__":
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
