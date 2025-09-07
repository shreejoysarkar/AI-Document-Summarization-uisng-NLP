from src.DocSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.DocSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from src.DocSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.DocSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.DocSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation Stage"
try:
     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
     data_validation = DataValidationPipeline()
     data_validation.main()
     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
