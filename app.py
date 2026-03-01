import streamlit as st
import pandas as pd
import pickle

# Load files
model = pickle.load(open("ipl_model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

st.title("🏏 IPL Match Winner Prediction")

st.write("Enter Match Details")

# --- USER INPUTS
team1 = st.selectbox("Team 1", sorted(le.classes_))
team2 = st.selectbox("Team 2", sorted(le.classes_))
toss_winner = st.selectbox("Toss Winner", sorted(le.classes_))
toss_decision = st.selectbox("Toss Decision", ["bat", "field"])
venue = st.text_input("Venue")

# Create dataframe from input
input_dict = {
    "team1": team1,
    "team2": team2,
    "toss_winner": toss_winner,
    "toss_decision": toss_decision,
    "venue": venue
}

input_df = pd.DataFrame([input_dict])

# Convert to dummy
input_encoded = pd.get_dummies(input_df)

# Add missing columns
for col in model_columns:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

# Reorder columns
input_encoded = input_encoded[model_columns]

# --- PREDICT
if st.button("Predict Winner"):

    prediction = model.predict(input_encoded)

    predicted_team = le.inverse_transform(prediction)

    st.success(f"🏆 Predicted Winner: {predicted_team[0]}")