# Streamlit Test

This project is structured for building a multi-page Streamlit and deploying it to Streamlit Community Cloud.

## Project Structure

- `app/main.py`: Streamlit entrypoint
- `app/pages/`: Multi-page screens
- `src/components/`: Reusable UI blocks
- `src/services/`: Data/API/business logic
- `src/utils/`: Helper functions
- `data/`: Local datasets for development
- `assets/`: Images/icons/static files
- `tests/`: Unit and integration tests
- `docs/`: Notes from PDF and implementation plan
- `.streamlit/config.toml`: Streamlit theme and settings

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

