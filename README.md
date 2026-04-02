# Streamlit Test

This repository contains a 33-page Streamlit lecture implementation split into neat, searchable files.

## Where the PDF Code Was Added

- `app/pages/02_text_and_display.py`
- `app/pages/03_input_widgets.py`
- `app/pages/04_layouts_containers.py`
- `app/pages/05_data_visualization.py`
- `app/pages/06_session_state_forms.py`
- `app/pages/07_multipage_navigation.py`
- `app/pages/08_caching_performance.py`
- `app/pages/09_ai_ml_integration.py`
- `app/pages/10_deployment_guide.py`
- `app/pages/11_best_practices.py`
- `src/utils/model_utils.py`

Full page-to-file mapping: `docs/pdf_code_map.md`

Raw extraction artifact: `docs/pdf_extracted_pages.txt`

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

## Run Tests

```bash
pytest -q
```

