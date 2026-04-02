import streamlit as st

st.title("Text, Markdown, and Display Elements")

st.header("Text Display")
st.subheader("Semantic headings")
st.text("Plain monospaced text")
st.write("Smart write auto-detects object types.")

st.markdown(
    """
## Markdown Section
- **Bold** and *italic* text
- `inline code` formatting
- [Streamlit](https://streamlit.io)
"""
)

st.code(
    """def predict(x):
    return model.predict(x)
""",
    language="python",
)

st.latex(r"\hat{y} = \sigma(W \cdot X + b)")
st.caption("Figure: Example mathematical notation")

st.header("Notification / Status Messages")
st.success("Model training completed successfully.")
st.info("Dataset loaded: 10,000 records found.")
st.warning("Missing values detected in 3 columns.")
st.error("Model file not found at models/clf.pkl")
st.toast("Predictions saved", icon=":white_check_mark:")

st.header("Metric Cards")
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Accuracy", value="94.5%", delta="+2.1%")
col2.metric(label="Precision", value="91.2%", delta="-0.8%")
col3.metric(label="Recall", value="96.3%", delta="+1.5%")
col4.metric(label="F1 Score", value="93.7%", delta="+0.6%")
st.metric("Loss", "0.082", delta="-0.014", delta_color="inverse")

st.header("JSON Display")
model_params = {
    "algorithm": "Random Forest",
    "n_estimators": 200,
    "max_depth": 15,
    "accuracy": 0.945,
    "features": ["age", "income", "score"],
}
st.json(model_params)
st.write(model_params)
