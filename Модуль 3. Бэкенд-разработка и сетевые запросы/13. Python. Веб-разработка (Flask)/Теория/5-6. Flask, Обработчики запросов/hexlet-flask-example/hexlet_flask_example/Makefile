install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install --force dist/*.whl

start:
	poetry run flask --app example --debug run --port 8000