import streamlit as st

st.title('My Machine Learning App')
st.write("This is a simple app for myML project.")

# You can add more components like buttons, text inputs, and sliders


import streamlit as st
import pickle
import numpy as np

st.title('Simple Machine Learning App')

model = pickle.load(open('model.pkl', 'rb'))

# Get input from user
feature_1 = st.number_input('Enter feature 1:')
feature_2 = st.number_input('Enter feature 2:')

if st.button('Predict'):
    result = model.predict(np.array([[feature_1, feature_2]]))
    st.write('The prediction is:', result)

    
feature = st.slider('Select a feature value', 0.0, 10.0, 5.0)
st.write(f'Selected value: {feature}')
