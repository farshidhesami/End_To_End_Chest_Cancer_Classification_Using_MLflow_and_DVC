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