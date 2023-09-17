# [Cervical Cancer Detection Web App](https://ahnngo-cervical-cancer-project-modelsapp-g6re8j.streamlitapp.com/): Project Overview
* Early detection of cervical cancer is crucial to reduce this disease's deadliness. Several predictive models are built based on data collected from 858 women from [UCI Machine Learning Repository](https://archive-beta.ics.uci.edu/ml/datasets/cervical+cancer+risk+factors) with 32 features and 4 targets, which are also the 4 most common tests for cervical cancer: Hinselmann, Schiller, Cytology, and Biopsy. 
* This dataset suffers from imbalance with only less than 9% positive patients and approximately 20% missing values. Besides, 32 attributes appear redundant to feed a predictive model, which may lead to potential overfitting. Therefore, several machine learning approaches have been deployed to deal with the aforementioned problems, such as feature engineering, resampling, and feature selection. The developer found that Support Vector Machine Classification, with the support of Border-SMOTE and Meta-transformer for selecting features based on importance weights for the Hinselmann, shows the most outstanding performance, with 8 chosen features, generating an accuracy of 98.18%.

## Code and Resources Used 
**Python Version:** 3.10

**Packages:** scikit-learn==0.24.1
streamlit~=1.10.0
joblib~=0.17.0
numpy~=1.22.1
pandas==1.4.2
matplotlib==3.5.1
imblearn==0.0

**Dataset:** https://archive-beta.ics.uci.edu/ml/datasets/cervical+cancer+risk+factors 

## Model performance
|    Test    |                        Model                        | No of Features | Accuracy | Precision | Sensitivity | Specificity |   F-1  |
|------------|:---------------------------------------------------:|:--------------:|:--------:|:---------:|:-----------:|:-----------:|:------:|
| Hinselmann |      SVM      + Borderline-SMOTE + Meta-transformer |        8       |  98.18%  |   98.76%  |    97.55%   |    98.80%   | 98.15% |
|  Schiller  | Random Forest + Borderline-SMOTE + Meta-transformer |        7       |  96.17%  |   96.58%  |    95.27%   |    96.97%   | 95.92% |
|  Citology  |      SVM      + Borderline-SMOTE + Meta-transformer |        6       |  97.54%  |   97.65%  |    97.65%   |    97.42%   | 96.74% |
|   Biopsy   | Random Forest + Borderline-SMOTE + Meta-transformer |        8       |  96.57%  |  100.00%  |    93.13%   |   100.00%   | 96.44% |
 

