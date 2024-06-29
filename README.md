# PatientSurvivalDetection 🏥💊 #

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
- In medical context, practitioners typical upload patient results to predict their survival. Hence, this application has the option to upload patient information of any no.
- Link: https://patientsurvivaldetection-gjfgzmmltdkgycabkjnrcz.streamlit.app/
