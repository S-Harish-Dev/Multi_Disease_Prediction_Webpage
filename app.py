import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# To Run: 
# python -m streamlit run app.py

# loading the saved model

diabeties_model = pickle.load(open('Model_save_Diabeties.sav','rb'))
Heart_model = pickle.load(open('Model_save_heart.sav','rb'))
Parkinson_model = pickle.load(open('Model_save.sav','rb'))


# sidebar for navigation

with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                            icons = ['activity','heart','person'], # taken from Bootstrap icon
                            default_index = 0)


# Diabeties Predictive Page

if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML' )

    # getting the input data from user
    # columns for input field 3 in a row
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        Blood_pressure = st.text_input('Blood_pressures')
    with col1:
        Skin_Thickness = st.text_input('Skin_Thickness')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI')
    with col1:
        Diabeies_Pedigree_Function = st.text_input('Diabeies_Pedigree_Function')
    with col2:
        age = st.text_input('Age')
    
    # code for prediction
    # creating a button for Prediction
    diabeties_dignosis = ''

    if st.button('Diabeties Test result'):
        diabeties_pred = diabeties_model.predict([[Pregnancies,Glucose,Blood_pressure,Skin_Thickness,Insulin,BMI,Diabeies_Pedigree_Function,age]])

        if (diabeties_pred[0] ==1):
            diabeties_dignosis = 'The Person is Diabetic'
        else:
            diabeties_dignosis = 'The Person is not Diabetic'

    st.success(diabeties_dignosis)


elif (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML' )

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1=male, 0=female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0-3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1=true, 0=false)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results (0-2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1=yes, 0=no)')
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Flourosopy')
    with col1:
        thal = st.text_input('Thalassemia (0-3)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        heart_pred = Heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if (heart_pred[0] ==1):
            heart_diagnosis = 'The Person has Heart Disease'
        else:
            heart_diagnosis = 'The Person does not have Heart Disease'
    
    st.success(heart_diagnosis)

elif (selected == 'Parkinson Prediction'):

    # page title
    st.title('Parkinson Prediction using ML' )

    col1, col2, col3 = st.columns(3)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col1:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        rap = st.text_input('MDVP:RAP')
    with col1:
        ppq = st.text_input('MDVP:PPQ')
    with col2:
        ddp = st.text_input('Jitter:DDP')
    with col3:
        shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        apq3 = st.text_input('Shimmer:APQ3')
    with col3:
        apq5 = st.text_input('Shimmer:APQ5')
    with col1:
        apq = st.text_input('MDVP:APQ')
    with col2:
        dda = st.text_input('Shimmer:DDA')
    with col3:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        d2 = st.text_input('D2')
    with col1:
        ppe = st.text_input('PPE')
    
    parkinson_diagnosis = ''

    if st.button('Parkinson Test Result'):
        parkinson_pred = Parkinson_model.predict([[fo,fhi,flo,jitter_percent,jitter_abs,rap,ppq,ddp,shimmer,shimmer_db,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]])

        if (parkinson_pred[0] ==1):
            parkinson_diagnosis = "The Person has Parkinson's Disease"
        else:
            parkinson_diagnosis = "The Person does not have Parkinson's Disease"
    
    st.success(parkinson_diagnosis)
