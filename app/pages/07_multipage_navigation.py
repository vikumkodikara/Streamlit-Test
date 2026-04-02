import streamlit as st

st.title("Multi-Page Apps and Navigation")

st.markdown(
    """
### File-Based Multipage Routing
Use numbered filenames in `app/pages/`:
- Prefixes like `01_`, `02_` control sidebar order.
- Underscores become spaces in page labels.
- Session state is shared across pages.
"""
)

st.header("Shared State Demo")
if "trained_model" not in st.session_state:
    st.session_state.trained_model = None

if st.button("Train Placeholder Model", type="primary"):
    st.session_state.trained_model = "model_placeholder"
    st.success("Model trained and saved to session")

if st.session_state.get("trained_model") is None:
    st.warning("No model found. Train first.")
else:
    st.success("Model loaded from session and ready")

st.header("Programmatic Navigation")
st.info("If your Streamlit version supports it, this button switches to another page.")
if st.button("Go to Data Visualization Page"):
    try:
        st.switch_page("app/pages/05_data_visualization.py")
    except Exception as exc:
        st.error(f"switch_page unavailable or path mismatch: {exc}")
