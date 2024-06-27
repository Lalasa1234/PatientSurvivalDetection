import streamlit as st
import keras
import numpy as np
from keras.saving import load_model
from keras.utils import normalize
import pandas as pd
import category_encoders as ce

model = load_model('Model/ModelCheckPoint/best_model.keras')

st.title('Prediction of Patient Survival')

uploaded_file = st.file_uploader('Please upload the Patients' details below to predict their chances of survival')

if uploaded_file is not None:
    df_temp = pd.read_csv(uploaded_file)

    ethnicity_options = ['Caucasian', 'Hispanic', 'African American', 'Asian']
    gender_options = ['F', 'M']
    h_admit_options = ['Acute Care/Floor', 'Operating Room', 'Emergency Department', 'Floor', 'Direct Admit', 'Other Hospital', 'PACU', 'Recovery Room', 'Step-Down Unit (SDU)']
    i_admit_options = ['Floor', 'Operating Room / Recovery', 'Accident & Emergency', 'Other Hospital']
    icu_stay_options = ['admit', 'transfer']
    icu_type_options = ['Med-Surg ICU', 'CSICU', 'CCU-CTICU', 'Cardiac ICU', 'Neuro ICU', 'SICU', 'CTICU', 'MICU']
    apache_3j_options = ['Sepsis', 'Cardiovascular', 'Metabolic', 'Neurological', 'Gastrointestinal', 'Musculoskeletal/Skin', 'Respiratory', 'Genitourinary', 'Trauma']
    apache_2_options = ['Cardiovascular', 'Metabolic', 'Neurologic', 'Gastrointestinal', 'Trauma', 'Respiratory', 'Renal/Genitourinary', 'Undefined Diagnoses']

    # Code for encoding
    for i in range(df_temp.shape[0]):
        df_temp['ethnicity'][i] = 1 + ethnicity_options.index(df_temp['ethnicity'][i])
        df_temp['gender'][i] = 1 + gender_options.index(df_temp['gender'][i])
        df_temp['hospital_admit_source'][i] = 1 + h_admit_options.index(df_temp['hospital_admit_source'][i])
        df_temp['icu_admit_source'][i] = 1 + i_admit_options.index(df_temp['icu_admit_source'][i])
        df_temp['icu_stay_type'][i] = 1 + icu_stay_options.index(df_temp['icu_stay_type'][i])
        df_temp['icu_type'][i] = 1 + icu_type_options.index(df_temp['icu_type'][i])
        df_temp['apache_3j_bodysystem'][i] = 1 + apache_3j_options.index(df_temp['apache_3j_bodysystem'][i])
        df_temp['apache_2_bodysystem'][i] = 1 + apache_2_options.index(df_temp['apache_2_bodysystem'][i])

    # Normalize and predict
    df_norm = normalize(np.array(df_temp).astype('float'))
    prediction = np.round(model.predict(df_norm))

    for i in range(prediction.shape[0]):
        if prediction[i] == 1:
            st.success(f'The patient #{i+1} is going to expire soon and needs specialized medication ')
        else:
            st.success(f'The patient #{i+1} will survive with the current medication. Hooray!')
