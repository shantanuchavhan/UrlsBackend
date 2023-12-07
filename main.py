from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database

DATABASE_URL = "postgresql://postgres:Shantanu8983@@localhost:5432/UrlTask"
database = Database(DATABASE_URL)
metadata = MetaData()

# Create the engine
engine = create_engine(DATABASE_URL)

# Define the products table
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

# Bind the table to the engine
metadata.create_all(bind=engine)

app = FastAPI()

# CORS middleware settings
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to insert product into the table
async def insert_product(product_data):
    query = products.insert().values(product_data)
    return await database.execute(query)

# Function to insert product with error handling
async def insert_product_through_code(product_data):
    try:
        await database.connect()
        await insert_product(product_data)
        print("Product inserted successfully")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        await database.disconnect()

# Function to create the table
async def create_table():
    print("hii")
    await database.connect()
    try:
        # The following line is not necessary as the table is created during metadata.create_all
        # await database.execute("DROP TABLE IF EXISTS products")
        print("Table created successfully")
    finally:
        await database.disconnect()

# API endpoint to insert a product
@app.post("/insert-product")
async def insert_product_api(product_data: dict):
    print(product_data, "ee")
    await create_table()
    try:
        await insert_product_through_code(product_data)
        return {"message": "Product inserted successfully"}
    except HTTPException as e:
        # If there's an HTTPException, return its details in the response
        return {"error": str(e)}
    except Exception as e:
        # If there's any other exception, return a generic error message
        return {"error": f"Internal Server Error: {str(e)}"}

# Other endpoints...
