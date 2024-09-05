from fastapi import FastAPI, UploadFile, Form, Response,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from fastapi import HTTPException
from typing import Annotated
import sqlite3
import hashlib


   
con = sqlite3.connect('db.db', check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()

app = FastAPI()

SECRET = "super-coding"
manager = LoginManager(SECRET, '/login')

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


@manager.user_loader()
def query_user(data):
    WHERE_STATEMENTS = f'id="{data}"'
    if type(data) == dict:
        WHERE_STATEMENTS = f'''id="{data['id']}"'''
    cur = con.cursor()

    user = cur.execute("""
                       SELECT * FROM users WHERE id=?
                       """,(WHERE_STATEMENTS,)).fetchone()
    return user

@app.post("/login")
async def login(id: str = Form(...),
                password: str = Form(...)):
         
    print(f"Received id:{id}, password:{password}")
    user = query_user(id)
    hashed_password = hash_password(password)
    print("User", user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
       
    elif user[3] != hashed_password:
        raise HTTPException(status_code=401, detail = "Invalid password")
       
    access_token = manager.create_access_token(data={
        'sub' : {
            'id':user['id'],
            'name':user['name'],
            'email':user['email'],
        }
    })

       

    
    return {'access_token':access_token} #return을 200으로 설정하지 않아도 자동으로 200을 내려줌. 

@app.post('/signup')
async def signup(id: Annotated[str, Form()],
                 name: Annotated[str, Form()],
                 email: Annotated[str, Form()],
                 password: Annotated[str, Form()]):
    
    hashed_password = hash_password(password)
    cur.execute(f"""
                INSERT INTO users(id, name, email, password)
                VALUES('{id}', '{name}', '{email}', '{hashed_password}')
                """)
    con.commit()
    return '200'

cur.execute(f"""
            CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            image BLOB,
            price INTEGER NOT NULL,
            description TEXT,
            place TEXT NOT NULL,
            insertAt INTEGER NOT NULL
);
""")
con.commit()

@app.post('/items')
async def create_item(image: UploadFile,
                title: Annotated[str, Form()],
                price: Annotated[int, Form()],
                description: Annotated[str, Form()],
                place: Annotated[str, Form()],
                insertAt: Annotated[int, Form()]):
               
    image_bytes = await image.read()
    cur.execute(f"""
                INSERT INTO
                items(title, image, price, description, place, insertAt)
                VALUES ('{title}', '{image_bytes.hex()}', {price}, '{description}', '{place}', {insertAt})
                """)
    con.commit()
    return '200'
@app.get('/items')
async def get_items(user=Depends(manager)):
    con.row_factory = sqlite3.Row
    cur = con.cursor()
 
    rows = cur.execute(f"""
                      SELECT * FROM items;
                      """).fetchall()
    return JSONResponse(content=(dict(row) for row in rows))

@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor()
    image_bytes = cur.execute(f"""
                              SELECT image FROM items WHERE id={item_id}
                              """).fetchone()[0]
   
    return Response(content=bytes.fromhex(image_bytes), media_type='image/*')



app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
