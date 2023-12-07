from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException


from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database




DATABASE_URL = "postgresql://postgres:Shantanu8983@@localhost:5432/UrlTask"

database = Database(DATABASE_URL)
metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("Product/Service", String),
    Column("price", Integer),
    Column("quantity", Integer),
    Column("unit", String),
    Column("weight", Integer),
    Column("description", String),
)



app = FastAPI()





 # 
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)
#










@app.get("/")
async def root():
    print("hii")
    return {"message": "Hello World"}


@app.get("/terms")
async def root():
    return {"message": "VED Å klikke på Fakturere Nå så velger dere å laste ned ifølge den informasjon som dere har lagt inn og teksten på last ned siden og vilkårene her, og aksepterer samtidig vilkårene her."}

@app.get("/us")
async def root():
    return {"message": "VED Å klikke på Fakturere Nå så velger dere å laste ned ifølge den informasjon som dere har lagt inn og teksten på last ned siden og vilkårene her, og aksepterer samtidig vilkårene her."}



@app.get("/ok")
async def root():
    print("hii")
    return{"message":"hii pro level"}


@app.get("/getProducts")
async def root():
    print("getting")
    return {"message": [
    [
        658313245,
        "Product 1",
        74373,
        965146,
        "Piece",
        50,
        "Description for Product 1"
    ],
    [
        4662520676,
        "Product 2",
        94422,
        1488416,
        "Piece",
        31,
        "Description for Product 2"
    ],
    [
        5620616523,
        "Product 3",
        21004,
        1102736,
        "Liter",
        55,
        "Description for Product 3"
    ],
    [
        5795135149,
        "Product 4",
        5355,
        1057295,
        "Kg",
        25,
        "Description for Product 4"
    ],
    [
        2792474651,
        "Product 5",
        36471,
        1866439,
        "Liter",
        67,
        "Description for Product 5"
    ],
    [
        3992986810,
        "Product 6",
        85011,
        1940633,
        "Liter",
        69,
        "Description for Product 6"
    ],
    [
        1585499227,
        "Product 7",
        73032,
        462132,
        "Liter",
        54,
        "Description for Product 7"
    ],
    [
        7164454206,
        "Product 8",
        31852,
        1173817,
        "Liter",
        37,
        "Description for Product 8"
    ],
    [
        1842725101,
        "Product 9",
        80751,
        147466,
        "Piece",
        22,
        "Description for Product 9"
    ],
    [
        3134255904,
        "Product 10",
        63057,
        897078,
        "Liter",
        5,
        "Description for Product 10"
    ],
    [
        5961243443,
        "Product 11",
        83079,
        355441,
        "Piece",
        14,
        "Description for Product 11"
    ],
    [
        3176823143,
        "Product 12",
        93498,
        150544,
        "Kg",
        11,
        "Description for Product 12"
    ],
    [
        4068386366,
        "Product 13",
        50369,
        1833492,
        "Kg",
        38,
        "Description for Product 13"
    ],
    [
        5529130347,
        "Product 14",
        29339,
        1033242,
        "Kg",
        37,
        "Description for Product 14"
    ],
    [
        9551193865,
        "Product 15",
        38089,
        1451108,
        "Kg",
        93,
        "Description for Product 15"
    ],
    [
        6488284121,
        "Product 16",
        11967,
        1329809,
        "Liter",
        0,
        "Description for Product 16"
    ],
    [
        4127634226,
        "Product 17",
        79386,
        1540097,
        "Liter",
        8,
        "Description for Product 17"
    ],
    [
        4336397227,
        "Product 18",
        65413,
        336714,
        "Kg",
        20,
        "Description for Product 18"
    ],
    [
        1094843927,
        "Product 19",
        66161,
        420710,
        "Liter",
        79,
        "Description for Product 19"
    ],
    [
        9379837477,
        "Product 20",
        97488,
        969639,
        "Piece",
        2,
        "Description for Product 20"
    ]
]}
