install:
	poetry install

test:
	poetry run pytest

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint8:
	poetry run flake8 brain_games

make flake-game:
	poetry run flake8 brain_games/game.py

.PHONY: install test
