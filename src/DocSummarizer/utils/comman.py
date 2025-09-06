# comman.py

import os
from box.exceptions import BoxValueError
import yaml
from docsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"The file {path_to_yaml} is empty.")
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Error converting to ConfigBox: {e}")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list[Path]) -> None:
    """Creates directories if they do not exist.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory {path} created successfully or already exists.")

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of the file in KB.
    """
    size_in_bytes = round(os.path.getsize(path) / 1024)
    return f"{size_in_bytes} KB"
