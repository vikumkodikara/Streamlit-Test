import numpy as np
import streamlit as st

st.title("AI and ML Integration Patterns")

st.header("Scikit-learn Style Inference Pattern")
st.code(
    """@st.cache_resource
def load_model(path):
    import pickle
    with open(path, 'rb') as f:
        return pickle.load(f)
""",
    language="python",
)

with st.form("predict_form"):
    col1, col2 = st.columns(2)
    age = col1.number_input("Age", 18, 100, 45)
    glucose = col1.number_input("Glucose Level", 50, 300, 120)
    bmi = col2.number_input("BMI", 10.0, 60.0, 25.0)
    bp = col2.number_input("Blood Pressure", 40, 200, 80)
    submitted = st.form_submit_button("Predict Risk", type="primary")

if submitted:
    features = np.array([[age, glucose, bmi, bp]])
    mock_prob = float(min(0.99, max(0.01, (features.mean() / 300))))
    label = "High Risk" if mock_prob > 0.5 else "Low Risk"
    c1, c2 = st.columns(2)
    c1.metric("Prediction", label)
    c2.metric("Probability", f"{mock_prob:.1%}")

st.header("Image Classification Pattern")
uploaded = st.file_uploader("Upload X-Ray Image", type=["jpg", "png", "jpeg"])
if uploaded:
    try:
        from PIL import Image

        img = Image.open(uploaded).convert("RGB")
        st.image(img, caption="Uploaded image", use_container_width=True)
        if st.button("Classify", type="primary"):
            st.info("Mock prediction: Healthy 78%, Pneumonia 15%, COVID-19 7%")
    except Exception as exc:
        st.error(f"Image processing failed: {exc}")

st.header("NLP / Chatbot Pattern")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about your FYP data..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = f'You asked: "{prompt}". Connect your LLM call here.'
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
