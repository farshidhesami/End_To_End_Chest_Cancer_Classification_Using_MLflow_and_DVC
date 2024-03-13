from pathlib import Path
import logging
import logging.config

# Basic configuration for the root logger
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def get_logger(name):
    
    """
    Creates or retrieves a logger with a specified name.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        # Create handler
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)

        # Add handler to the logger
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger

project_name = 'CnnChestCancerMLflowDVC'

# list of files to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configurations.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_model_trainer.py",
    f"src/{project_name}/pipeline/stage_05_model_evaluation.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "artifacts/data_ingestion",
    "artifacts/data_transformation",
    "artifacts/data_validation",
    "artifacts/model_evaluation",
    "artifacts/model_trainer",
    "data/sample.csv",
    "deployment-steps/sample.pdf",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "application.py",
    "requirements.txt",
    "setup.py",
    "research/01_data_ingestion.ipynb",
    "research/02_data_validation.ipynb",
    "research/03_data_transformation.ipynb",
    "research/04_model_trainer.ipynb",
    "research/05_model_evaluation.ipynb",
    "research/Experiment.ipynb",
    "research/trials.ipynb",
    "templates/index.html",
    "templates/results.html",
    "application.py",
    "template.py"

]

for filepath_str in list_of_files:      # Iterate over the list of files
    filepath = Path(filepath_str)       
    component = "general"               # Default logger name

    if "components" in filepath.parts:
        component = filepath.parts[2]   # Assume the structure is like src/ProjectName/components/ComponentName

    logger = get_logger(component)

    # Create parent directory if it doesn't exist
    filepath.parent.mkdir(parents=True, exist_ok=True)
    logger.info(f"Created or verified directory: {filepath.parent}")

    # Create or touch the file
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logger.info(f"Created or verified file: {filepath}")
    else:
        logger.info(f"{filepath.name} already exists")

