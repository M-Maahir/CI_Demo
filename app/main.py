from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():

    return{
        "message":"Maahir from feature branch one"
    }

@app.get("/users/{user}")
def users(user: str):
    return {
        "user":user
    }

@app.get('/names')
def names():
    return{
        "names":"Maahir is one of the name"
    }