## template.py is basiclly work as automated files crested by pyhton code 
import os 
from pathlib import Path
import logging


logging.basicConfig(
   
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


project_name = "data-science"

## List of files to be created automatcially by scripting 

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "schema.yaml",
    "setup.py", 
    "research/research.ipynb",
    "templates/index.html",
    # "requirements.txt",
    "app.py",

]


## template code for cresrting the file and folder automatically 

for file_path in list_of_files:
     file_path = Path(file_path)
     filedir, file_name = os.path.split(file_path)


     if filedir != "":
          os.makedirs(filedir, exist_ok=True)
          logging.info(f"Creating directory; {filedir} for the file: {file_name}")



     if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0): #not os.path.exists(file_path):
        with open(file_path, "w") as f:
             pass
        logging.info(f"Creating file: {file_name} at {filedir}")


     else:
        logging.info(f"File already exists: {file_name} at {filedir}, skipping creation.")  
          