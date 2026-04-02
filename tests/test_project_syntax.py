from pathlib import Path


PROJECT_FILES = [
    "app/main.py",
    "app/pages/01_overview.py",
    "app/pages/02_text_and_display.py",
    "app/pages/03_input_widgets.py",
    "app/pages/04_layouts_containers.py",
    "app/pages/05_data_visualization.py",
    "app/pages/06_session_state_forms.py",
    "app/pages/07_multipage_navigation.py",
    "app/pages/08_caching_performance.py",
    "app/pages/09_ai_ml_integration.py",
    "app/pages/10_deployment_guide.py",
    "app/pages/11_best_practices.py",
    "src/utils/model_utils.py",
]


def test_python_files_compile():
    for file_rel in PROJECT_FILES:
        path = Path(file_rel)
        source = path.read_text(encoding="utf-8")
        compile(source, str(path), "exec")
