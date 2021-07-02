.PHONY: test

test:
	docker-compose exec -d remember pytest --color=yes --showlocals --tb=short -v tests/unit
	docker-compose exec -d remember pytest --color=yes --showlocals --tb=short -v tests/integration
	docker-compose exec -d remember pytest --color=yes --showlocals --tb=short -v tests/e2e

linter:
	@isort --gitignore -n -l 80 --honor-noqa --color --om -q --sg .venv --sg docker .
	-@mypy --config-file mypy.ini ./src
	-@flake8 ./src
	@black -l 80 --color --exclude "/(\.venv|__pycache__|docker)/" -q .
	@echo "[+] linter successfully executed"

