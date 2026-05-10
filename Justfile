default:
    just --list --justfile "{{justfile()}}"

[private]
verify_with_impl python_minor_version $UV_PROJECT_ENVIRONMENT:
    uv sync --python 3.{{python_minor_version}}

    uv run -m mypy .
    uv run ty check .
    uv run ruff format --check --target-version py3{{python_minor_version}}
    uv run ruff check --target-version py3{{python_minor_version}}
    uv run -m pytest

verify_with python_minor_version="14": (verify_with_impl python_minor_version ".just_venv_3_"+python_minor_version)

verify: (verify_with "8") (verify_with "9") (verify_with "10") (verify_with "11") (verify_with "12") (verify_with "13") (verify_with "14")

build_no_verify:
    rm -rf dist
    uv build

build: verify build_no_verify
    rm -rf dist
    uv build

publish: build
    uv publish
