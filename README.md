# End_To_End_Chest_Cancer_Classification_Using_MLflow_and_DVC

### Create a template.py :

- For logging.basicConfig(filename='app.log', level=logging.INFO) for more information Go to website : https://docs.python.org/3/library/logging.html .

- Add a ".github/workflows/.gitkeep", in code because Git does not track empty directories by default, so adding a `.gitkeep` file is a common workaround
  to this.the `.gitkeep` file is not a built-in feature of Git. It's just a convention that many developers use.

- open a terminal and write a "python template.py" and check the app.log file is created or not.

- Add a "requirements.txt" file in a code and "setup.py" after that open a terminal and write a "pip install -r requirements.txt" .

- Go to the src\CnnChestCancerMLflowDVC and then click a "__init__.py" 

- For working Logger we need to create a another file "main.py" and write a code in it.
   - Note : for first stage just temporary write a  " logger.info("Welcome to CnnChestCancerMLflowDVC! ") " after first code and then run the "python main.py" in terminal.
    - Result of terminal :  [2024-03-14 10:17:41,256: INFO: main: Welcome to CnnChestCancerMLflowDVC! ]

- Why we use a utils folder ? 
  - The `utils` directory (or `utilities` or `helpers`) is commonly used in many projects to store utility functions or classes.
  - The purpose of the `utils` directory is to promote code reuse and reduce duplication. Instead of writing the same code in multiple places, you can write it once in a utility
    function and then call that function wherever you need it.  

- Go to the src\utils and create a "common.py" and write a code in it.  

### This is Workflows : 

- 1- Update config.yaml
- 2- Update secrets.yaml [Optional]
- 3- Update params.yaml
- 4- Update the entity
- 5- Update the configuration manager in src config
- 6- Update the components
- 7- Update the pipeline
- 8- Update the main.py
- 9- Update the dvc.yaml  


- Upload a "Chest-CT-Scan-data.zip" in "https://drive.google.com/" 

### How download a data from google drive : (see research/trials.ipynb) 
- import gdown
- Copy link from google drive and paste it in code.(Don t forget to manage a access to "Anyone with the link can view" in google drive)
- Copy a link to code url = "https://drive.google.com/file/d/1eB4WPSWYFWgXmkwGteICvvum9eGYHUFe/view?usp=sharing"
- There is a file Id in google drive link " 1eB4WPSWYFWgXmkwGteICvvum9eGYHUFe " and this id help us to download a file from google drive. 
- Extract id code with type a code " type(url) ".
- Split a url code with type a code " url.split("/") ".
- Define a prefix code with type a code prefix = "https://drive.google.com/uc?id=" .
   -Add a code :  prefix = 'https://drive.google.com/uc?/export=download&id='
                  gdown.download(prefix+file_id, "Chest-CT-Scan-data.zip")