# Intelligent Streamlit FYP Application

This is a multi-page Streamlit application built as a Final Year Project proof-of-concept.  
It demonstrates data exploration, model workflow simulation, evaluation views, prediction interfaces, chatbot-style interaction, and deployment-ready project organization.

## Features

- Data explorer workflows for uploaded datasets
- Model training simulation with session state
- Evaluation dashboards with metrics and charts
- Prediction interface with user inputs
- Chat-style interaction page
- Caching examples for performance optimization
- Modular structure for maintainability and scaling
- Streamlit Cloud deployment-ready setup

## Project Structure

```text
Streamlit-Test/
├── app/
│   ├── main.py
│   └── pages/
│       ├── overview.py
│       ├── text_and_display.py
│       ├── input_widgets.py
│       ├── layouts_containers.py
│       ├── data_visualization.py
│       ├── session_state_forms.py
│       ├── multipage_navigation.py
│       ├── caching_performance.py
│       ├── ai_ml_integration.py
│       ├── deployment_guide.py
│       └── best_practices.py
├── src/
│   ├── components/
│   ├── services/
│   └── utils/
│       └── model_utils.py
├── tests/
│   ├── test_model_utils.py
│   └── test_project_syntax.py
├── docs/
│   ├── pdf_code_map.md
│   └── pdf_extracted_pages.txt
├── data/
├── assets/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── requirements.txt
└── .gitignore
```

## Installation and Setup

1. Clone your repository.

```bash
git clone <your-repo-url>
cd Streamlit-Test
```

2. Create a virtual environment.

```bash
python -m venv .venv
```

3. Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

## Running Locally

```bash
streamlit run app/main.py
```

After running, open http://localhost:8501 in your browser.

## Running Tests

```bash
pytest -q
```

## Deployment (Streamlit Community Cloud)

1. Push the latest code to GitHub.
2. Open https://share.streamlit.io and sign in.
3. Create a new app and select your repository and main branch.
4. Set the app entry file to app/main.py.
5. Add required secrets in the Streamlit Cloud app settings.
6. Deploy.

## Configuration

The app uses .streamlit/config.toml for server and theme settings.

Use .streamlit/secrets.toml.example as a template for local secrets and Streamlit Cloud secrets.

## Notes

- The lecture-note implementation is mapped in docs/pdf_code_map.md.
- Extracted PDF text used for organization is in docs/pdf_extracted_pages.txt.
- This project is intended for academic and educational use.


