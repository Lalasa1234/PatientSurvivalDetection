# PatientSurvivalDetection #

**Involves heavy data cleaning and preprocessing**
- Outlier capping based on the APACHE3 medical standards
- Auto EDA using autoviz

**Deep Learning Model using Keras**
- Optuna-based Hyperparameter tuning and Kerascheckback to prune inefficient trials
- Model checkpoint to save the best model state
- Early stopping and logging
- TensorBoard graphic visualization

**Deployment**
- In medical context, practitioners typical upload patient results to predict their survival.
- Hence, the application has an option to upload patient information of any no.
