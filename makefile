.PHONY: help install lint format pytest mypy docs

help:
	@echo "Available commands:"
	@echo "  install                    Install dependencies using Poetry"
	@echo "  lint                       Run linters using pre-commit"
	@echo "  format                     Run formatters using pre-commit"
	@echo "  pytest                     Run tests using pytest"
	@echo "  mypy                       Run type-checking using mypy"
	@echo "  docs                       Generate documentation using lazydocs"

install:
	poetry install

lint:
	pre-commit run ruff --all-files

format:
	pre-commit run ruff-format --all-files

pytest:
	poetry run pytest

mypy:
	poetry run mypy --ignore-missing-imports easy_gui_prompt

docs:
	poetry run lazydocs --overview-file="README.md" easy_gui_prompt

.DEFAULT_GOAL := help