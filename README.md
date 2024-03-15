# End_To_End_Chest_Cancer_Classification_Using_MLflow_and_DVC

## Chest Cancer Classification - VVG16 :
- The classification of chest cancer using VGG16 involves a deep learning approach to identify and categorize various types of chest cancers based on imaging data, such as CT scans or X-rays. The VGG16 model, known for its effectiveness in image recognition tasks, can be adapted for this purpose through a process called transfer learning. This process leverages pre-trained weights and fine-tunes the model to recognize specific patterns associated with different chest cancers.

### Diagnosis : 
- Diagnosis typically involves a combination of imaging tests, biopsies, and laboratory tests:
Imaging Tests: CT scans, MRIs, PET scans, and chest X-rays are used to visualize the tumor and assess its size, location, and possible spread.
Biopsy: A sample of the suspicious tissue is removed and examined under a microscope to confirm the presence of cancer cells.
Blood Tests: Certain markers in the blood can indicate cancer, though they are not definitive diagnostic tools on their own.


### Deep Learning in Diagnosis:
- The application of VGG16 for chest cancer classification involves training the model to recognize and differentiate between benign and malignant tumors based on patterns in the imaging data. This approach requires a large dataset of annotated images (images labeled with the correct diagnosis) to train the model effectively. The model learns to extract and interpret complex features from the images, enabling it to predict the presence of cancer in new, unseen images.

- In practice, this could greatly assist radiologists by providing a preliminary assessment of scans, highlighting areas of concern, and potentially speeding up the diagnosis process. However, the final diagnosis should always be confirmed by a medical professional through comprehensive clinical evaluation and diagnostic testing.

### What is the VGG16 :
- VGG16 is a significant model in the field of computer vision, particularly for image recognition tasks. Developed by Karen Simonyan and Andrew Zisserman from the University of Oxford, the model was introduced in their paper "Very Deep Convolutional Networks for Large-Scale Image Recognition." It stands out due to its simplicity and depth, consisting of 16 layers that are convolutional or fully connected. VGG16 is known for its high accuracy on the ImageNet dataset, achieving 92.7% top-5 test accuracy. This dataset is a large-scale repository that contains over 14 million images categorized into 1000 classes. VGG16’s architecture, which utilizes 3x3 convolution filters and 2x2 pooling layers arranged in a deep sequence, has been influential in the development of convolutional neural networks (CNNs) for various applications.

### Description :
- In the context of chest cancer classification, the images are prepared in common image formats (JPG or PNG) instead of medical imaging formats like DICOM (Digital Imaging and Communications in Medicine), to be compatible with the VGG16 model. The dataset is divided into three categories representing different types of chest cancer (Adenocarcinoma, Large cell carcinoma, Squamous cell carcinoma) and a category for normal cells. This dataset is structured into three main folders:

- Training set (70% of the data): Used to train the model, adjusting its weights based on the provided labels.
Testing set (20% of the data): Used to evaluate the model's performance on unseen data, providing an estimate of its generalization ability.
Validation set (10% of the data): Used during the model training process to adjust hyperparameters and prevent overfitting.

### Types of Chest Cancer in the Dataset :
- Adenocarcinoma: The most common form of lung cancer, primarily found in the outer regions of the lung. It is characterized by tumors in the glands that secrete mucus and is associated with symptoms such as coughing, hoarseness, weight loss, and weakness.

- Large Cell Carcinoma: A type of lung cancer that grows and spreads quickly, potentially appearing anywhere in the lung. It accounts for 10 to 15 percent of non-small cell lung cancer (NSCLC) cases and is noted for its rapid progression.

- Squamous Cell Carcinoma: This lung cancer type is located centrally in the lung, near the larger bronchi and main airway branches. Linked to smoking, it constitutes about 30 percent of NSCLC cases.

### Application of VGG16 for Chest Cancer Classification:
- Using the VGG16 model for chest cancer classification involves training the model on the dataset described, allowing it to learn distinguishing features between the different cancer types and normal cells. The model can be fine-tuned by adjusting the final layers to classify images into one of the four categories. Transfer learning, where the pre-trained weights of VGG16 (trained on ImageNet) are adapted to this specific task, can significantly enhance the learning process and model performance due to the similar nature of image recognition tasks. This application leverages deep learning's capabilities to assist in diagnosing and differentiating types of chest cancers, potentially improving the accuracy and efficiency of medical diagnoses.

## Start a project :

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

### How download a data from google drive : (see research/trials.ipynb) :
- import gdown
- Copy link from google drive and paste it in code.(Don t forget to manage a access to "Anyone with the link can view" in google drive)
- Copy a link to code url = "https://drive.google.com/file/d/1eB4WPSWYFWgXmkwGteICvvum9eGYHUFe/view?usp=sharing"
- There is a file Id in google drive link " 1eB4WPSWYFWgXmkwGteICvvum9eGYHUFe " and this id help us to download a file from google drive. 
- Extract id code with type a code " type(url) ".
- Split a url code with type a code " url.split("/") ".
- Define a prefix code with type a code prefix = "https://drive.google.com/uc?id=" .
   -Add a code :  prefix = ..........

### Data_ingestion : 
- Now implement this code into the " research/01_data_ingestion.ipynb " .
- Update config.yaml and params.yaml : before make data class code Update a "config.yaml" and "params.yaml" but in params.yaml file just add a "key: val" and after
  compleat a model fill it . 
- Update the entity : Go to " research/01_data_ingestion.ipynb " 
- Update the configuration manager in src config : before create a code in "src / nnChestCancerMLflowDVC / constants / __init__.py" and go to research/01_data_ingestion.ipynb and write a code .
- Update the pipeline 
