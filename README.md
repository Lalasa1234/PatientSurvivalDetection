### PatientSurvivalDetection 🏥💊 ###
___

**Business Application in Hospitals**

To help medical practitioners predict the chances of patient survival proactively based on multiple variables on demographic, vitals, labs results, labs blood gas, APACHE covariate, prediction, comorbidity and grouping. Based on the prediction, the treatments could be hyper-personalized.

**Problem Statement**

The target feature is hospital_death which is a binary variable. The task is to classify this variable based on the other 84 features based on the scoring metric: Area under ROC curve and Recall (this is important as the cost and risk of model predicting death is higher than the model predicting life)

___

### Step-by-step Methodology 🪜📄 ###

**Data cleaning and preprocessing**
- Outlier capping based on the APACHE3 medical standards
- Auto EDA using autoviz

**Deep Learning Model Building and Evaluation using Keras**
- Optuna-based Hyperparameter tuning and Kerascheckback to prune inefficient trials
- Model checkpoint to save the best model state
- Backtracking the Streamlit results to verify the model's prediction

**Results**

- Validation AUC of 84% and Recall of 78%

**Application UI**
- In medical context, practitioners typical upload patient results. Hence, this application has the option to upload patient information (.csv).
  
  Note: TestData_Patients is available in the Dataset folder
- Link: https://patientsurvivaldetection-gjfgzmmltdkgycabkjnrcz.streamlit.app/

___

 **Next Steps 📃☑️✅**
 - Log results on MLFlow
 - Showcase the results on DagsHub
