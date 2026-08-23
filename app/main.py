from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return{
        "message":"Maahir from feature branch one"
    }

@app.get("/users")
def users(user: dict):
    return {
        "user":user
    }