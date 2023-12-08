from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database
import random



app = FastAPI()

# CORS middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/terms")
async def get_terms():
    return {"message": "VED Å klikke på Fakturere Nå så velger dere å laste ned ifølge den informasjon som dere har lagt inn og teksten på last ned siden og vilkårene her, og aksepterer samtidig vilkårene her."}

@app.get("/us")
async def get_us():
    return {"message": "VED Å klikke på Fakturere Nå så velger dere å laste ned ifølge den informasjon som dere har lagt inn og teksten på last ned siden og vilkårene her, og aksepterer samtidig vilkårene her."}


@app.get("/getAllProduct")
async def root():
    return {"message":[[7465000852,"Product 1",93881,632235,"Kg",58,"Description for Product 1"],[5752106165,"Product 2",46280,465899,"Liter",47,"Description for Product 2"],[2422695555,"Product 3",42880,1171347,"Liter",79,"Description for Product 3"],[2581987276,"Product 4",98764,867344,"Liter",16,"Description for Product 4"],[6233241536,"Product 5",70659,1939737,"Liter",50,"Description for Product 5"],[1571769736,"Product 6",71091,184941,"Liter",68,"Description for Product 6"],[8252392448,"Product 7",12173,741082,"Kg",4,"Description for Product 7"],[4173937893,"Product 8",66715,774322,"Kg",85,"Description for Product 8"],[1733876550,"Product 9",26408,133300,"Kg",65,"Description for Product 9"],[4876386493,"Product 10",54156,1706394,"Piece",89,"Description for Product 10"],[2800441092,"Product 11",12397,1400929,"Kg",54,"Description for Product 11"],[9200764438,"Product 12",1280,524818,"Kg",70,"Description for Product 12"],[9619323085,"Product 13",85612,1187133,"Kg",69,"Description for Product 13"],[9080206171,"Product 14",65100,460234,"Piece",25,"Description for Product 14"],[6699514855,"Product 15",81104,1044044,"Kg",11,"Description for Product 15"],[9272130698,"Product 16",12225,462301,"Piece",19,"Description for Product 16"],[2571472752,"Product 17",7019,1380450,"Kg",15,"Description for Product 17"],[8620922048,"Product 18",55420,1840476,"Liter",9,"Description for Product 18"],[4521660667,"Product 19",85446,740732,"Piece",1,"Description for Product 19"],[7853266096,"Product 20",92019,1027648,"Liter",47,"Description for Product 20"]]}


