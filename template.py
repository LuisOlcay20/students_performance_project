'''
This file allows the creation/modification of the structure for the project

'''

import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(messahe)s:' )

project_name = "students_performance_project"


list_of_files = [
    ".github.com/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/components/__init__.py", #Modules that we need 
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/pipeline/__init__.py",  #Pipeline that we need 
    f"src/pipeline/train_pipeline.py",
    f"src/pipeline/predict_pipeline.py",
    f"src/logger.py",
    f"src/exception.py",
    f"src/utils.py",
    "app.py",
    "requirements.txt",
    "setup.py",

    ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}") 

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    
    else:
        logging.info(f"{filename} is already exists")