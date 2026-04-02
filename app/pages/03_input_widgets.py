from datetime import date, time

import pandas as pd
import streamlit as st

st.title("Input Widgets")

st.header("Text and Number Inputs")
name = st.text_input("Enter your name", value="Student", max_chars=50)
api_key = st.text_input("API Key", type="password")
notes = st.text_area("Research Notes", height=150, placeholder="Describe your methodology...")
threshold = st.number_input(
    "Classification Threshold",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01,
    format="%.2f",
)
st.write(f"Hello, {name}. Positive class threshold: {threshold}")
if api_key:
    st.info("API key captured in-memory for this session.")

st.header("Selection Widgets")
model_type = st.selectbox(
    "Select Model",
    options=["Logistic Regression", "Random Forest", "SVM", "Neural Network", "XGBoost"],
    index=1,
)
features = st.multiselect(
    "Select Features",
    options=["age", "income", "education", "score", "region"],
    default=["age", "income"],
)
split_method = st.radio(
    "Train/Test Split Method",
    options=["Hold-out (80/20)", "K-Fold CV", "Stratified K-Fold"],
    horizontal=True,
)
normalise = st.checkbox("Normalise features", value=True)
show_conf_matrix = st.checkbox("Show Confusion Matrix")

st.write(
    {
        "model_type": model_type,
        "features": features,
        "split_method": split_method,
        "normalise": normalise,
        "show_conf_matrix": show_conf_matrix,
    }
)

st.header("Sliders and Ranges")
n_trees = st.slider("Number of Trees", min_value=10, max_value=500, value=100, step=10)
age_range = st.slider("Age Range Filter", min_value=18, max_value=80, value=(25, 55))
date_range = st.slider(
    "Date Range",
    min_value=date(2020, 1, 1),
    max_value=date(2025, 12, 31),
    value=(date(2022, 1, 1), date(2024, 12, 31)),
)
st.write(f"n_trees={n_trees}, age_range={age_range}, date_range={date_range}")

st.header("Buttons and File Inputs")
if st.button("Train Model", type="primary"):
    with st.spinner("Training in progress..."):
        st.success("Training complete")

df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
csv = df.to_csv(index=False)
st.download_button("Download Results as CSV", data=csv, file_name="predictions.csv", mime="text/csv")

dob = st.date_input("Date of Birth", min_value=date(1950, 1, 1), max_value=date.today())
start_time = st.time_input("Start Time", value=time(9, 0))
st.write({"dob": dob, "start_time": start_time})

uploaded = st.file_uploader("Upload Dataset (CSV)", type=["csv"])
if uploaded:
    up_df = pd.read_csv(uploaded)
    st.success(f"Loaded {len(up_df)} rows and {len(up_df.columns)} columns")
    st.dataframe(up_df.head(), use_container_width=True)

images = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
st.write(f"{len(images)} image(s) uploaded")
