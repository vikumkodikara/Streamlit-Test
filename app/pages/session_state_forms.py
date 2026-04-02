import streamlit as st

st.title("Session State and Reactivity")

st.header("Counter with Session State")
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

if st.button("Reset Counter"):
    st.session_state.count = 0

st.write(f"Count: {st.session_state.count}")

st.header("ML Workflow-like Session Keys")
defaults = {
    "model": None,
    "training_history": [],
    "current_dataset": None,
    "predictions": None,
    "is_trained": False,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def on_model_change() -> None:
    st.session_state.model = None
    st.session_state.is_trained = False
    st.toast("Model reset - please retrain.", icon="⚠️")


algorithm = st.selectbox("Algorithm", ["Random Forest", "SVM", "XGBoost"], on_change=on_model_change)
st.write(f"Selected algorithm: {algorithm}")

if st.button("Train Model", type="primary"):
    st.session_state.is_trained = True
    st.session_state.training_history.append({"epoch": len(st.session_state.training_history) + 1, "accuracy": 0.94})
    st.success("Model ready")

if st.session_state.is_trained:
    st.success(f"Model trained - {len(st.session_state.training_history)} run(s)")
else:
    st.warning("Please train the model first")

st.header("Forms - Batch Submission")
with st.form("patient_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 0, 120, 35)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with col2:
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)

    symptoms = st.multiselect("Symptoms", ["Fever", "Cough", "Fatigue", "Breathlessness"])
    notes = st.text_area("Clinical Notes")
    submitted = st.form_submit_button("Run Diagnosis", type="primary")

if submitted:
    bmi = weight / ((height / 100) ** 2)
    st.metric("BMI", f"{bmi:.1f}")
    st.info(f"Processing {age}yr {gender} patient with {len(symptoms)} symptoms")
    if notes:
        st.write("Notes received")
