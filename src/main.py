from fastapi import FastAPI

app = FastAPI(
    title="trade APP",
    version="0.0.1"
)


@app.get('/')
def hello():
    return 'Hello, app!'
