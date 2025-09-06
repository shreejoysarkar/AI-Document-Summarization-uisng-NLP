from src.DocSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.DocSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
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
