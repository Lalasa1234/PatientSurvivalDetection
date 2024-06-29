### PatientSurvivalDetection 🏥💊 ###
___

**Objective**
To predict the chances of patient survival based on multiple variables on demographic, vitals, labs results, labs blood gas, APACHE covariate, prediction, comorbidity and grouping.

**Involves heavy data cleaning and preprocessing**
- Outlier capping based on the APACHE3 medical standards
- Auto EDA using autoviz

**Deep Learning Model using Keras**
- Optuna-based Hyperparameter tuning and Kerascheckback to prune inefficient trials
- Model checkpoint to save the best model state
- Backtracking the Streamlit results to verify the model's prediction

**Deployment**
- In medical context, practitioners typical upload patient results. Hence, this application has the option to upload patient information in the form of .csv files.
  TestData_Patients![image](https://github.com/Lalasa1234/PatientSurvivalDetection/assets/166985767/7bf36c6a-6f24-42a3-8250-c3586aebe279)

- Link: https://patientsurvivaldetection-gjfgzmmltdkgycabkjnrcz.streamlit.app/
