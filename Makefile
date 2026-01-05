ifneq ("$(wildcard .env)","")
    include .env
    export $(shell sed 's/=.*//' .env)
endif

rebuild:
	poetry export -f requirements.txt --output=requirements.txt --without-hashes
	docker build -t fastapi_portfolio .
	rm requirements.txt
	docker rm -f test-fastapi
	docker stop portfolio_db
	docker run -d -p ${LOCALHOST_PORT}:5435 --name test-fastapi fastapi_portfolio
	docker start portfolio_db

dev:
	docker start portfolio_db
	docker start test-fastapi
