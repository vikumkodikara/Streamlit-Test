import streamlit as st

st.title("Deployment Guide")

st.header("Streamlit Community Cloud")
st.markdown(
    """
1. Push code to GitHub.
2. Ensure `requirements.txt` is in repository root.
3. Go to Streamlit Community Cloud and create a new app.
4. Set entrypoint to `app/main.py`.
5. Add secrets in app settings.
"""
)

st.header("Secrets Management")
st.code(
    """[api_keys]
openai_key = 'sk-xxxxxxxx'

[database]
host = 'localhost'
port = 5432
password = 'mypassword'
""",
    language="toml",
)

st.header("Render/Railway Start Command")
st.code(
    "streamlit run app/main.py --server.port $PORT --server.headless true",
    language="bash",
)

st.header("Dockerfile Pattern")
st.code(
    """FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
ENTRYPOINT [\"streamlit\", \"run\", \"app/main.py\", \"--server.port=8501\", \"--server.address=0.0.0.0\", \"--server.headless=true\"]
""",
    language="dockerfile",
)
