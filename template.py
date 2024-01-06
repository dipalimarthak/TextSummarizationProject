import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'textSummarizerProject'

list_of_files = [
    ".github/workflows/.gitkeep", #for cicd deployment
    "src/(project_name)/__init__.py",#this constructor file is used for local deployment
    "src/(project_name)/components/__init__.py/",#another local package
    "src/(project_name)/utils/__init__.py",#utils related code
    "src/(project_name)/utils/common.py",
    "src/(project_name)/logging/__init__.py",
    "src/(project_name)/config/__init__.py",
    "src/(project_name)/config/configuration.py",
    "src/(project_name)/pipeline/__init__.py",#training and prediction pipeline
    "src/(project_name)/entity/__init__.py",
    "src/(project_name)/comstants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",#build docker image and deploy docker image
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

#code to create files above


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    #check if file directory is not empty
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

        #now create the file   
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
