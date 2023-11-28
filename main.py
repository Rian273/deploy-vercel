from fastapi import FastAPI, HTTPException, Request
import pandas as pd

# key untuk akses endpoint
key = "secret123"

# panggil class FastAPI
app = FastAPI()

# # read file csv
# data = pd.read_csv('data.csv')

@app.get('/')
def handler():
    return {"message": "hello"}


# define url/endpoint
@app.get('/secret')
def handler(request: Request):

    # retrieve content form request
    headers = request.headers

    #retrieve User-Agent key in headers
    agent = headers.get("User-Agent")
    token = headers.get("Token")

    #jika key token tidak ada dalam headers
    if token == None:
        return{
            "message": "belum log in"
            }
    else: # jika ada key token
        if token != key: # jika token != key, raise error/exception
            raise HTTPException(status_code=500, detail="key tidak sesuai")
        return {
            'message': 'Main Page',
            "agent": agent # display value 'agent' in response
        }

# # merubah data csv menjadi dict/json
# @app.get('/data')
# def handler():
#     return data.to_dict(orient='records')

@app.get('/home/{user}')
def handler(user):
    if user == 'maudy':
        return {
            'message': 'Welcome Home',
            'user': user
        }
    else:
        # handle error: gunanya agar jika banyak org yg akses sistemnya ga down
        raise HTTPException(status_code=400, detail='not found')