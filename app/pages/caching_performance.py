import time

import pandas as pd
import streamlit as st

st.title("Caching and Performance")


@st.cache_data
def load_dataset(filepath: str) -> pd.DataFrame:
    time.sleep(0.2)
    return pd.read_csv(filepath)


@st.cache_data(ttl=3600)
def fetch_live_data(api_url: str) -> dict:
    import requests

    return requests.get(api_url, timeout=10).json()


@st.cache_resource
def get_db_connection():
    import sqlite3

    return sqlite3.connect(":memory:", check_same_thread=False)


st.markdown("""
- `@st.cache_data`: serializable results like DataFrames and API responses.
- `@st.cache_resource`: long-lived resources like DB/model connections.
""")

sample_csv = "data/sample_cache.csv"
if st.button("Create sample CSV"):
    pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}).to_csv(sample_csv, index=False)
    st.success(f"Wrote {sample_csv}")

if st.button("Load cached data"):
    try:
        df = load_dataset(sample_csv)
        st.dataframe(df, use_container_width=True)
    except Exception as exc:
        st.error(f"Load failed: {exc}")

if st.button("Clear data cache"):
    load_dataset.clear()
    st.success("Cache for load_dataset cleared")

if st.button("Clear all caches"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success("All caches cleared")

conn = get_db_connection()
st.caption(f"DB connection established: {conn is not None}")
