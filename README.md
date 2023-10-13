## kidney-disease-classification

The Kidney Tumor Dataset is a comprehensive collection of medical imaging data designed for the purpose of detecting and diagnosing various kidney conditions. This dataset encompasses a wide range of kidney images, including normal kidneys, cysts, tumors, and kidney stones. It serves as a valuable resource for researchers and healthcare professionals in the field of medical image analysis and diagnosis.



### How To Run?

**STEPS**:

  1. **Clone the repo**
     ```bash
     https://github.com/Prashantkhobragade/kidney-disease-classification.git
     ```
  2. **Create Conda env with python = 3.10.0**

  3. **Install requirements**
     
     ``` pip install -r requirements.txt```
     
  5. **Finally run**
     
     ``` python app.py ```


### Data Source:

This dataset is sourced from Kaggle and is provided by the user nazmul0087. You can access the dataset on Kaggle using the following link: [Kidney Tumor Dataset](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone).



### MLflow

  * Its Production Grade
  * Trace all of your experiments
  * Logging & tagging your model
  * Web UI for visualization


I am using DagsHub for remote repositories. To get started, you will need to log in to DagsHub with your GitHub account, provide access to this repository, and collect the following environment variables.

```bash
MLFLOW_TRACKING_URI=
MLFLOW_TRACKING_USERNAME=
MLFLOW_TRACKING_PASSWORD=
python script.py

```

**Set all variables:**
  - using cmd:
    
    ```set MLFLOW_TRACKING_URI=https://dagshub.com/Prashantkhobragade/kidney-disease-classification.mlflow

    set MLFLOW_TRACKING_USERNAME=

    set MLFLOW_TRACKING_PASSWORD=
    ```

 - using git bash

    ```
    export MLFLOW_TRACKING_URI=https://dagshub.com/Prashantkhobragade/kidney-disease-classification.mlflow

    export MLFLOW_TRACKING_USERNAME=

    export MLFLOW_TRACKING_PASSWORD=
    
    ```

### DVC

  - It's very lightweight for POC only
  - for experiments tracking
  - It can perform Orchestration (Creating Pipeline)

 **DVC cmd**
  1. dvc init
  2. dvc repro
  3. dvc dag

## AWS CI-CD Deployment with GitHub Action

  1. **Login to AWS console**
  2. **Create IAM user for deployment**
       - steps for deployment
           1. Build docker image of the source code
           2. push your docker image to ECR
           3. launch your EC2
           4. Pull your image from ECR in EC2
           5. Launch your docker image in EC2
        - Policy:
            1. AmazonEC2ContainerRegistryFullAccess
            2. AmazonEC2FullAccess
  3. **Create ECR repo to store docker Image**

     ``` save the ecr uri ```

  5. **Create EC2 machine Ubuntu**
  6. **open EC2 and Install Docker in Ec2 machine**
      ```#optinal

          sudo apt-get update -y

          sudo apt-get upgrade

          #required

          curl -fsSL https://get.docker.com -o get-docker.sh

          sudo sh get-docker.sh

          sudo usermod -aG docker ubuntu

          newgrp docker

          docker --version
      ```
  7. **Configure EC2 as self-hosted runner**
       ```
       setting>actions>runner>new self hosted runner> choose os (linux)> then run command one by one
       ```
   8. **Setup Github secrets**
```AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION =

AWS_ECR_LOGIN_URI = before / part from ecr uri

ECR_REPOSITORY_NAME = after / from ecr uri
```

### Project Focus
  - The main focus of this project is not to develop ML model but to Introduce MlOps Tools such as MLflow and DVC(data version control) and explore deployment in the AWS cloud infrastructure.

  - Due to resource constrain the model is trained on the subset of the dataset for only 2 Epochs with a learning rate of 0.001. I got a validation accuracy of 50%.

  - Please feel free to explore this dataset and associated code and documentation to better understand our approach and contribution to the advancement of the project
