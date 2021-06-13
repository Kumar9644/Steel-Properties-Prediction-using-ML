import streamlit as st
from joblib import *
model =load('steel_1.ml')

def predict():
    st.title('Made of Steel')
    st.image('stee2.jpg')
    st.write('Please Enter steel composition')
    c=st.number_input('Enter Carbon content')
    si = st.number_input('Enter Silicon content')
    mn= st.number_input('Enter Manganese content')
    p= st.number_input('Enter Phosphorus content')
    s= st.number_input('Enter sulphur content')
    ni = st.number_input('Enter Nickle content')
    cr = st.number_input('Enter Chromium content')
    mo= st.number_input('Enter Molybednum content')
    cu = st.number_input('Enter copper content')
    v= st.number_input('Enter Vanadiumm content')
    al = st.number_input('Enter Aluminium content')
    n= st.number_input('Enter Niterogen content')
    temp = st.number_input('Temperature(K)')
    if st.button('Predict UTS(Mpa)'):
        array=[c,si,mn,p,s,ni,cr,mo,cu,v,al,n,temp]
        y_pred=model.predict([array])
        st.success(y_pred[0])











if __name__ == '__main__':
    predict()
