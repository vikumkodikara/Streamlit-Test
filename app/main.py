import streamlit as st

st.set_page_config(
    page_title="My FYP Streamlit App",
    page_icon="📘",
    layout="wide",
)

st.title("My FYP Streamlit App")
st.write("Project scaffold is ready. Start implementing code from your PDF modules.")

st.subheader("Suggested Next Steps")
st.markdown("""
1. Add each PDF section into `app/pages/` as separate pages.
2. Move reusable logic into `src/services/` and `src/utils/`.
3. Keep UI components in `src/components/`.
4. Add tests in `tests/`.
""")
