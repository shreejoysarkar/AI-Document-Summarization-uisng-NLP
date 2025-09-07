from src.DocSummarizer.config.configuration import ConfigurationManager
from src.DocSummarizer.components.data_transformation import DataTransformation
from src.DocSummarizer.logging import logger


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()