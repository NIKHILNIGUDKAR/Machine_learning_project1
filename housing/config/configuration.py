from housing.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig, \
ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from housing.util.util import read_yaml_file

from housing.constant import *
from housing.exception import HousingException
import os,sys
import os





class Configuration:

    def __init__(self,
                 config_file_path:str=CONFIG_FILE_PATH,
                 current_time_stamp:str=CURRENT_DATE_STAMP
                 )-> None:
                try:
                     self.congfig_info =read_yaml_file(file_path=config_file_path)
                     self.training_pipeline_config =self.get_training_pipeline_config()
                     self.time_stamp=current_time_stamp
                except Exception as e:
                     raise HousingException(e,sys) from e

    def get_ingestion_config(self)->DataIngestionConfig:
        try:
            data_ingestion_info=self.congfig_info.config
            dataset_download_url
            tgz_download_dir
            raw_data_dir
            ingested_train_dir
            ingested_test_dir
             data_ingestion_config=DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                tgz_download_dir=tgz_download_dir,
                raw_data_dir=raw_data_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir, 
                )   

                logging.info(f"Data Ingestion config":{})
            except Exception as e:
              raise HousingException(e,sys) from e
              
        

    def get_data_validation_config(self)->DataValidationConfig:
        pass

    def get_data_transformation_config(self)->DataTransformationConfig:
        pass

    def get_model_trainer_config(self)->ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self)->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
         try:
              training_pipeline_config=self.congfig_info[TRAINING_PIPELINE_CONFIG_KEY]
              artifact_dir= os.path.join(ROOT_DIR,
              training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
              training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
              pass
         except Exception as e:
              raise HousingException(e,sys) from e