import uvicorn


if __name__ == "__main__":
    config = uvicorn.Config(app="app.main:app", host="0.0.0.0", port=5435, log_level="info")
    server = uvicorn.Server(config)
    server.run()