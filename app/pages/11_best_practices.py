import streamlit as st

st.title("Best Practices and FYP Checklist")

st.header("Common Pitfalls")
st.markdown(
    """
- Use `@st.cache_resource` for model loading.
- Use `st.session_state` instead of global variables.
- Call `st.set_page_config` as the first Streamlit call.
- Wrap file parsing in `try/except` and use `st.stop()` on validation failures.
- Keep secrets in `st.secrets`, never in source code.
"""
)

st.header("Demo Checklist")
checks = [
    "Test with fresh uploaded data",
    "Add spinners for slow operations",
    "Highlight key metrics: Accuracy/Precision/Recall/F1",
    "Include About section",
    "Test deployed URL before presentation",
]
for idx, item in enumerate(checks, start=1):
    st.checkbox(f"{idx}. {item}", value=False)

st.header("Quick Reference")
st.table(
    {
        "Category": ["Display", "Chart", "Layout", "Widget", "State", "Cache"],
        "Command": ["st.write", "st.plotly_chart", "st.columns", "st.selectbox", "st.session_state", "@st.cache_data"],
    }
)
