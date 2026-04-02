import time

import streamlit as st

st.title("Layouts and Containers")

st.header("Columns")
col1, col2, col3 = st.columns(3)
col1.metric("Accuracy", "94.5%", "+2%")
col2.metric("Loss", "0.082", "-0.01", delta_color="inverse")
col3.metric("F1", "93.7%", "+1%")

left, right = st.columns([2, 1])
with left:
    st.subheader("Prediction Results")
    st.write("Results table placeholder")
with right:
    st.subheader("Controls")
    threshold = st.slider("Threshold", 0.0, 1.0, 0.5)
    st.write(f"Threshold: {threshold}")

st.header("Sidebar")
with st.sidebar:
    st.title("FYP Controls")
    dataset = st.selectbox("Dataset", ["Train", "Test", "Validation"])
    model = st.selectbox("Model", ["RF", "SVM", "XGBoost"])
    n_estimators = st.slider("n_estimators", 10, 500, 100)
    run_btn = st.button("Run Experiment", type="primary")

st.write(f"Main area values: {model} on {dataset}, trees={n_estimators}")
if run_btn:
    st.info("Running experiment")

st.header("Tabs")
tab1, tab2, tab3, tab4 = st.tabs(["Data Overview", "Model Training", "Evaluation", "Predictions"])
with tab1:
    st.write("Dataset overview content")
with tab2:
    st.write("Training controls")
with tab3:
    c1, c2 = st.columns(2)
    c1.metric("Accuracy", "94.5%")
    c2.metric("F1 Score", "93.7%")
with tab4:
    st.write("Live predictions inputs")

st.header("Expanders, Container, and Status")
with st.expander("Advanced Configuration", expanded=False):
    learning_rate = st.number_input("Learning Rate", 0.0001, 0.1, 0.001)
    batch_size = st.selectbox("Batch Size", [16, 32, 64, 128])
    st.write({"learning_rate": learning_rate, "batch_size": batch_size})

result_container = st.empty()
if st.button("Generate Report"):
    result_container.success("Report generated")

with st.container(border=True):
    st.subheader("Model Summary")
    st.write("Algorithm: Random Forest | Trees: 200 | Depth: 15")

if st.button("Run Progress Demo"):
    progress = st.progress(0, text="Initialising...")
    for epoch in range(25):
        time.sleep(0.02)
        progress.progress((epoch + 1) * 4, text=f"Training epoch {epoch + 1}/25")
    progress.empty()

with st.spinner("Loading model weights..."):
    time.sleep(0.2)
st.success("Model loaded")

with st.status("Running pipeline...", expanded=True) as status:
    st.write("Loading data...")
    time.sleep(0.1)
    st.write("Preprocessing features...")
    time.sleep(0.1)
    st.write("Running inference...")
    status.update(label="Done", state="complete")
