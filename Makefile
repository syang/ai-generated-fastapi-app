.PHONY: test run

test:
	docker-compose run --rm test

run:
	docker-compose up --build
