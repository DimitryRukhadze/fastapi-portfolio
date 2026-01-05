rebuild:
	docker build -t fastapi_portfolio .
	docker rm -f test-fastapi
	docker stop portfolio_db
	docker run -d -p 8000:5435 --name test-fastapi fastapi_portfolio
	docker start portfolio_db

dev:
	docker start portfolio_db
	docker start test-fastapi
