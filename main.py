from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database
import random
from faker import Faker

DATABASE_URL = "postgresql://postgres:Shantanu8983@@localhost:5432/UrlTask"

database = Database(DATABASE_URL)
metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("ArticleNo",Integer ),  # Changed to use underscore instead of /
    Column("Product", String),
    Column("inPrice", Integer),
    Column("Price", Integer),
    Column("Unit", String),
    Column("inStock", Integer),
    Column("Description", String),
)



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

# Function to initialize database connection pool
async def startup():
    await database.connect()

# Function to close database connection pool
async def shutdown():
    await database.disconnect()

# Event handlers for startup and shutdown
app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

# Function to insert product into the database
async def insert_product(product_data):
    query = products.insert().values(product_data)
    return await database.execute(query)

fake = Faker()






async def get_products():
    query = products.select()
    return await database.fetch_all(query)


# import random

# def generate_random_data(count):
#     data = []
#     for i in range(count):
#         random_article_no = random.randint(1, 10000000000)
#         random_product_name = f"Product {i + 1}"
#         random_in_price = random.randint(1, 100000)
#         random_price = random.randint(1, 2000000)
#         random_unit = random.choice(['Piece', 'Kg', 'Liter'])
#         random_in_stock = random.randint(1, 100)
#         random_description = f"Description for Product {i + 1}"

#         data.append(
#             {
#                 "ArticleNo":random_article_no,
#                 "Product": random_product_name,
#                 "inPrice": random_in_price,
#                 "Price": random_price,
#                 "Unit":  random_unit,
#                 "inStock": random_in_stock,
#                 "Description": random_description 
#             }
#         )
#     return data

# # Example usage:
# random_data = generate_random_data(5)
# print(random_data)




# Route to add product
@app.post("/add-product")
async def add_product(product_data: dict):
    product_id = await insert_product(product_data)
    return {"message": f"Product added with ID: {product_id}"}

# Generate 20 product data
async def add_products(product_data: dict):
    product_id = await insert_product(product_data)
    return {"message": f"Product added with ID: {product_id}"}









@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/terms")
async def get_terms():
    return {"message": "VED Å klikke på Fakturere Nå så velger dere å laste ned ifølge den informasjon som dere har lagt inn og teksten på last ned siden og vilkårene her, og aksepterer samtidig vilkårene her.Dere kan bruke programmet GRATIS i 14 dager.LettFaktura er så lett og selvforklarende at sjansen for at du vil komme til å trenge support er minimal, men hvis du skulle trenge support, så er vi her for deg, med vårt kontor bemannet større delen av døgnet. Etter prøveperioden så fortsetter abonnementet og koster 99 kroner eks. mva per måned, som faktureres årlig. Hvis du ikke ønsker å beholde programmet, så er det bare til å avbryte prøveperioden ved å gi beskjed innen 14 dager fra nedlasting.Dere har selvfølgelig rett til å avslutte bruken av programmet uten kostnad, ved å gi oss beskjed per email innen 14 dager fra nedlasting, om at dere ikke ønsker å fortsette med programmet, og betaler da selvfølgelig ikke heller noe"}

@app.get("/us")
async def get_us():
    return {"message": "Your US message here"}


@app.get("/getProducts")
async def get_products_route():
    products_data = await get_products()
    converted_list = [
            [product["ArticleNo"], product["Product"], product["inPrice"], product["Price"],
            product["Unit"], product["inStock"], product["Description"]]
            for product in products_data
        ]
    print(converted_list,"converted_list")
    return {"message": converted_list}