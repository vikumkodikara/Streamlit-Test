from pathlib import Path


PROJECT_FILES = ["app/main.py", "src/utils/model_utils.py"]


def _page_files() -> list[Path]:
    return sorted(Path("app/pages").glob("*.py"))


def test_python_files_compile():
    for file_rel in PROJECT_FILES:
        path = Path(file_rel)
        source = path.read_text(encoding="utf-8")
        compile(source, str(path), "exec")

    for path in _page_files():
        source = path.read_text(encoding="utf-8")
        compile(source, str(path), "exec")
