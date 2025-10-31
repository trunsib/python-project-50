install:
		uv install

gendiff:
		uv run gendiff

test:
		uv run pytest

test-coverage:
		uv run pytest --cov=gendiff --cov-report xml

publish:
		uv publish --dry-run

package-install:
		python3 -m pip install --force-reinstall --user dist/*.whl

lint:
		uv run flake8 gendiff

selfcheck:
		uv check

check: selfcheck test lint

build: check
		uv build

.PHONY: install test lint selfcheck check build