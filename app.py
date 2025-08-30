import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

with open('model.pkl', 'rb') as f:
    regressor = pickle.load(f)
st.title("Startup Profit Prediction")

st.header("Enter Startup Details:")

min_rd, max_rd = 0, 165350
min_admin, max_admin = 0, 182645
min_market, max_market = 0, 471785

rd_spend = st.slider("R&D Spend", min_value=min_rd, max_value=max_rd, value=min_rd, format="%.2f")
administration = st.slider("Administration Spend", min_value=min_admin, max_value=max_admin, value=min_admin, format="%.2f")
marketing_spend = st.slider("Marketing Spend", min_value=min_market, max_value=max_market, value=min_market, format="%.2f")

state = st.selectbox("State", ('New York', 'California', 'Florida'))
is_florida = 1 if state == 'Florida' else 0
is_new_york = 1 if state == 'New York' else 0

if st.button("Predict Profit"):
    input_data = pd.DataFrame([[rd_spend, administration, marketing_spend, is_florida, is_new_york]],
                              columns=['R&D Spend', 'Administration', 'Marketing Spend', 'Florida', 'New York'])
    predicted_profit = regressor.predict(input_data)[0]
    st.success(f"Predicted Profit: ${predicted_profit:,.2f}")
