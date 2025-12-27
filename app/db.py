from sqlalchemy import create_engine, text


engine = create_engine("postgresql+psycopg2://postgres:oER810TR@localhost:5432/postgres", echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 'Hello, World!'"))
    print(result.all())
