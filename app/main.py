import streamlit as st

st.set_page_config(
    page_title="My FYP Streamlit App",
    page_icon="📘",
    layout="wide",
)

st.markdown(
    """
<style>
.hero-card {
    padding: 2rem;
    border-radius: 16px;
    background: linear-gradient(120deg, #f8fafc 0%, #e2e8f0 100%);
    border: 1px solid #cbd5e1;
}
.hero-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.6rem;
}
.hero-text {
    font-size: 1.05rem;
    line-height: 1.7;
    color: #334155;
    max-width: 900px;
}
</style>

<div class="hero-card">
  <div class="hero-title">This Is My Testing Application</div>
  <div class="hero-text">
    This project is a multi-page Streamlit application built as a final year proof-of-concept.
    It brings together data exploration, model workflow demonstrations, evaluation dashboards,
    prediction interfaces, and deployment-ready structure in one clean and practical system.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")
st.info("Use the left sidebar to navigate through each module of the application.")

