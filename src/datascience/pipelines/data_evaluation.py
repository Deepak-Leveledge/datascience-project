from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_evaluation import ModelEvaluation
from src.datascience import logger



STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def initiate_model_evaluation(self):
        config= ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()