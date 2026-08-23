from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return{
        "message":"This is the main get method"
    }

@app.get("/users")
def users(user: dict):
    return {
        "user":user
    }