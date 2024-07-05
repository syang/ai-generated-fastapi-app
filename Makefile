.PHONY: test run clean

test:
	docker-compose run --rm test

run:
	# Start FastAPI service
	uvicorn main:app --reload

clean:
	# Remove Python cache files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	
	# Remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	
	# Remove coverage and test result files
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	
	# Remove Docker-related files if any
	docker-compose down -v --rmi all

