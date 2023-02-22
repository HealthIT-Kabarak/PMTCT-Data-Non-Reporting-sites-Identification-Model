# PMTCT-Data-Non-Reporting-sites-Identification-Model

### 1.1 Dev Name:
    Isaac Kiplangat - icheruiyot823@gmail.com
    Winfred Muusi - gmuusi@kabarak.ac.ke
    Jacob Mutiso - jmuasa@kabarak.ac.ke
    Ividah Francis - ividah@kabarak.ac.ke
    Limo Duke - 
### 1.2 Problem Statement:
The problem being addressed is the inconsistent reporting of the HIV Testing Indicator across facilities, where some facilities include tests from some testing locations and exclude PMTCT tests. This inconsistency in reporting can lead to inaccurate data, making it challenging to identify gaps in HIV testing and treatment.

To address this issue, a data science/AI approach was applied to identify different data behaviors, advise on estimates where data gaps are found, and automate the clean-up of the data. The goal was to develop a classification model to assist in the identification of PMTCT sites that do not report tests, improving the consistency and accuracy of HIV testing indicators across facilities.

The story around this problem is one of improving healthcare outcomes through the use of data science and AI. By identifying gaps in HIV testing and treatment, healthcare providers can make data-driven decisions to improve patient care and reduce the spread of HIV. The use of machine learning models, such as the decision tree model, can help automate this process, saving time and resources while improving the accuracy of HIV testing data.


### 1.3 Data Engineering 

The data engineering process involves transforming and preparing raw data into a format that is suitable for analysis. Here is an outline of the data engineering process that may have been followed for the problem of identifying PMTCT sites that do not report tests:

#### 1.3.1 Data collection: 
The first step in the data engineering process is to collect data from various sources. For this problem, data on HIV testing indicators from various facilities may have been collected.

#### 1.3.2 Data cleaning: 
Once the data has been collected, it needs to be cleaned to remove any missing or invalid values. This process may involve imputing missing data, correcting errors, and removing duplicates.

#### 1.3.3 Data integration:
If the data comes from multiple sources, it may need to be integrated into a single dataset. This involves combining data from different sources into a single dataset and resolving any inconsistencies or discrepancies.

#### 1.3.4  Data transformation: 
Once the data is cleaned and integrated, it may need to be transformed to make it suitable for analysis. This may involve feature selection, feature engineering, scaling, and normalization.

#### 1.3.5 Data splitting: 
The data is split into training and testing datasets. The training dataset is used to build the machine learning model, while the testing dataset is used to evaluate the performance of the model.

#### 1.3.6 Data preprocessing: 
Before the data is used to train the machine learning model, it may need to be preprocessed. This may involve one-hot encoding categorical variables, standardizing numerical variables, and handling missing values.

### 1.4 Modelling : 
Once the data is preprocessed, it is used to train the machine learning model. The model may be a decision tree, logistic regression, or another classification algorithm.

#### 1.4.1 Model evaluation: 
The performance of the model is evaluated using the testing dataset. Metrics such as accuracy, precision, recall, and F1 score may be used to evaluate the model's performance.

#### 1.4.2 Model optimization: 
If the model's performance is not satisfactory, it may need to be optimized. This involves tweaking the hyperparameters of the model, changing the algorithm, or adding more features to the dataset.

#### 1.4.3 Model deployment:

Once the model is optimized and its performance is satisfactory, it can be deployed in a production environment to assist in the identification of PMTCT sites that do not report tests.

Overall, the data engineering process is critical to the success of a machine learning project. It involves collecting, cleaning, integrating, transforming, splitting, preprocessing, training, evaluating, optimizing, and deploying data to build a machine learning model that can solve the problem at hand.

### 1.5 Installation
   #### 1.5.1: Git Clone
        https://github.com/HealthIT-Kabarak/PMTCT-Data-Non-Reporting-sites-Identification-Model.git
   
   #### 1.5.2 Creating virtual environment
         python<version> -m venv <virtual-environment-name>
   
   #### 1.5.3 Installing necessary libraries
        pip install <packagename>
   

integrating the developed classification model into an application or system that can be used by stakeholders to identify PMTCT sites that do not report tests.
