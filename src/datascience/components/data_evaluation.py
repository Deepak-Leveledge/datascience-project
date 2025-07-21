import os
from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import joblib
import numpy as np
import yaml

from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.common import save_json


os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/deepakleveledge/datascience-project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "deepakleveledge"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "47eca7011c5c3a5e283716c5052a11b5ec816099"

class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae= mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(columns=[self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme



        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            score={"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metrics_file_name), data=score)


            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(score)
            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)



            ## model registry
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")





    