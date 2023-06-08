install:
	poetry install

test:
	poetry run pytest

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint8:
	poetry run flake8 brain_games

.PHONY: install test
