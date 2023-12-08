from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database
import random
from faker import Faker

DATABASE_URL = "postgresql://postgres:Shantanu8983@@localhost:5432/UrlTask"

# database = Database(DATABASE_URL)
# metadata = MetaData()

# products = Table(
#     "products",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("ArticleNo",Integer ),  # Changed to use underscore instead of /
#     Column("Product", String),
#     Column("inPrice", Integer),
#     Column("Price", Integer),
#     Column("Unit", String),
#     Column("inStock", Integer),
#     Column("Description", String),
# )



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
# async def startup():
#     await database.connect()

# Function to close database connection pool
# async def shutdown():
#     await database.disconnect()

# # Event handlers for startup and shutdown
# app.add_event_handler("startup", startup)
# app.add_event_handler("shutdown", shutdown)

# # Function to insert product into the database
# async def insert_product(product_data):
#     query = products.insert().values(product_data)
#     return await database.execute(query)

# fake = Faker()




# async def get_products():
#     query = products.select()
#     return await database.fetch_all(query)




# # Route to add product
# @app.post("/add-product")
# async def add_product(product_data: dict):
#     product_id = await insert_product(product_data)
#     return {"message": f"Product added with ID: {product_id}"}

# # Generate 20 product data
# async def add_products(product_data: dict):
#     product_id = await insert_product(product_data)
#     return {"message": f"Product added with ID: {product_id}"}









@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/terms")
async def get_terms():
    return {"message": "VED Å klikke på Fakturere Nå så velger dere å laste ned ifølge den informasjon som dere har lagt inn og teksten på last ned siden og vilkårene her, og aksepterer samtidig vilkårene her.Dere kan bruke programmet GRATIS i 14 dager.LettFaktura er så lett og selvforklarende at sjansen for at du vil komme til å trenge support er minimal, men hvis du skulle trenge support, så er vi her for deg, med vårt kontor bemannet større delen av døgnet. Etter prøveperioden så fortsetter abonnementet og koster 99 kroner eks. mva per måned, som faktureres årlig. Hvis du ikke ønsker å beholde programmet, så er det bare til å avbryte prøveperioden ved å gi beskjed innen 14 dager fra nedlasting.Dere har selvfølgelig rett til å avslutte bruken av programmet uten kostnad, ved å gi oss beskjed per email innen 14 dager fra nedlasting, om at dere ikke ønsker å fortsette med programmet, og betaler da selvfølgelig ikke heller noe. Hvis vi ikke innen 14 dager fra nedlasting mottar slik beskjed fra dere, så kan ordren av naturlige grunner ikke endres. Med nedlasting menes den dato og klokkeslett når dere har valgt å trykke på knappen Fakturere Nå. Fakturering skjer for ett år av gangen. Prisen for LettFaktura (tilbudspris kr 99,- per måned / ord. pris kr 129,- per måned) er for årsavgift Start for ett års bruk av programmet.(Ved bruk av tilbudsprisen kr 99,- så regnes ett års perioden fra nedlastning.) Alle priser er eks. mva. Timeregistrering. Kalkulering, Medlemsfakturering, Tilbud, Kunde Oppfølging, Lager Telling, Lagerstyring og Engelsk fakturatekst er tilleggsmoduler som kan bestilles etter installasjon av programmet.Årsavgiften er løpende men hvis dere ikke ønsker å fortsette å bruke programmet, så er det bare å gi beskjed tretti dager før starten av den nestfølgende ett års perioden. Introduksjonstilbudet (kr 99,- per måned) er for årsavgift Start for det første året.  Etter det første året faktureres ord. pris hvilket for tiden er, for årsavgift Start, ett hundre og tjueni kroner per måned, for årsavgift Fjernstyring, to hundre og sekstifem kroner per måned og for årsavgift Pro, tre hundre og trettitre kroner per måned. Etter ett år faktureres årsavgift Fjernstyring som standard men dere kan velge Start eller Pro ved å gi beskjed når som helst før forfall. Hvis dere velger å beholde programmet ved å ikke gi oss beskjed per email innen 14 dager fra nedlasting, om at dere ikke ønsker å fortsette med programmet, så aksepterer dere at dere kommer å betale fakturaen for deres bestilling. Kode til programmet vil sendes automatisk etter at fakturaen er betalt. Å ikke betale fakturaen eller sen betaling gir ikke rett til å annullere bestillingen. Vi hjelper gjerne å fikse logo for dere til selvkostpris. Lisens for bruk av LettFaktura selges selvfølgelig i følge gjeldende lover. For å lettere kunne hjelpe dere og gi dere support samt for å følge lovene  må vi av naturlige grunner lagre deres informasjon.I forbindelse med lagring av informasjon så krever loven at vi gir dere følgende informasjon:Hvis dere bestiller som privatperson så har dere den angrerett som loven tilsier. Deres informasjon lagres slik at vi kan hjelpe dere m.m. Vi kommer til å bruke den for å kunne hjelpe dere hvis dere trenger hjelp, følge lovene vedr. bokføring m.m. Når det kommer oppgraderinger og lignende, kan vi komme til å sende dere tilbud og lignende om våre produkter og tjenester per email eller lignende. Dere kan komme til å bli kontaktet per email, post og telefon. Hvis dere ikke ønsker å bli kontaktet, bare send oss en email vedr. det.Dere kan når som helst be om å ikke få tilsendt informasjon om oppgraderinger per email, faks, brev eller lignende og vi kommer da selvfølgelig ikke å gjøre det. Slik begjæring sender dere til oss per email, faks, brev eller lignende. Av naturlige grunner må vi lagre, databehandle og flytte deres data. Deres informasjon lagres inntil videre. Dere gir oss tillatelse til å lagre, databehandle og flytte deres data, samt å sende dere tilbud og lignende per email, faks, brev og lignende. Grunnet måten det fungerer på med programvare trenger tillatelsen også å gis til andre parter. Tillatelsen gis derfor til oss, samt til de bedrifter og/eller person/personer som eier programvaren, kildekoden, hjemmesiden og lignende. Det gis også til nåværende og fremtidige bedrifter eiet og/eller kontrollert av en eller flere av de som i dag eier og/eller kontrollerer oss. Det gis også til nåværende og fremtidige bedrifter eiet og/eller kontrollert av en eller flere av de som i dag eier og/eller kontrollerer de bedrifter, (om noen), som eier eller kommer til å eie programvaren, kildekoden, hjemmesiden og lignende. Det gis også til nåværende og fremtidige personer (om noen) som eier eller kommer til å eie programvaren, kildekoden, hjemmesiden og lignende. Dette både for nåværende og fremtidige produkter og tjenester. Det gis også til annen bedrift, som vi kan bruke for å sende/selge produkter, oppgraderinger og lignende, enten ved underlisensiering eller på annen måte. Dere har selvfølgelig rett å begjære å få del av, endre og slette informasjonen vi holder om dere. Dere har også rett å begjære begrensing av databehandlingen, og å protestere mot databehandlingen og retten til dataportabilitet. Dere har rett å klage til tilsynsmyndighet. Mer juridisk info om oss finner dere . Det er lovene i Irland som er gjeldende lover. Det er selvfølgelig helt frivillig å legge ordre. Vi bruker selvsagt ikke noen automatisert profileringer eller beslutninger. Hvis dere ønsker å kontakte oss, vennligst bruk da informasjonen på denne eller noen av våre andre hjemmesider. Vår erfaring er at våre kunder er meget fornøyde med måten vi jobber på og håper og tror at det også kommer til å bli deres opplevelse.Ha en flott dag!"}

@app.get("/us")
async def get_us():
    return {"message": "We that dispose of and drive this homepage and that also sell the programs that are sold on this homepage are: Lettfaktura Ltd, registered in Ireland with company number 638535. Registered office is in Co. Laois, Ireland.We hope that you will have much joy and use of our homepage.Have a still great day!"}


# @app.get("/getProducts")
# async def get_products_route():
#     products_data = await get_products()
#     converted_list = [
#             [product["ArticleNo"], product["Product"], product["inPrice"], product["Price"],
#             product["Unit"], product["inStock"], product["Description"]]
#             for product in products_data
#         ]
#     print(converted_list,"converted_list")
#     return {"message": products_data}


@app.get("/getAllProduct")
async def root():
    data=[{"id":63,"ArticleNo":7465000852,"Product":"Product 1","inPrice":93881,"Price":632235,"Unit":"Kg","inStock":58,"Description":"Description for Product 1"},{"id":64,"ArticleNo":5752106165,"Product":"Product 2","inPrice":46280,"Price":465899,"Unit":"Liter","inStock":47,"Description":"Description for Product 2"},{"id":65,"ArticleNo":2422695555,"Product":"Product 3","inPrice":42880,"Price":1171347,"Unit":"Liter","inStock":79,"Description":"Description for Product 3"},{"id":66,"ArticleNo":2581987276,"Product":"Product 4","inPrice":98764,"Price":867344,"Unit":"Liter","inStock":16,"Description":"Description for Product 4"},{"id":67,"ArticleNo":6233241536,"Product":"Product 5","inPrice":70659,"Price":1939737,"Unit":"Liter","inStock":50,"Description":"Description for Product 5"},{"id":68,"ArticleNo":1571769736,"Product":"Product 6","inPrice":71091,"Price":184941,"Unit":"Liter","inStock":68,"Description":"Description for Product 6"},{"id":69,"ArticleNo":8252392448,"Product":"Product 7","inPrice":12173,"Price":741082,"Unit":"Kg","inStock":4,"Description":"Description for Product 7"},{"id":70,"ArticleNo":4173937893,"Product":"Product 8","inPrice":66715,"Price":774322,"Unit":"Kg","inStock":85,"Description":"Description for Product 8"},{"id":71,"ArticleNo":1733876550,"Product":"Product 9","inPrice":26408,"Price":133300,"Unit":"Kg","inStock":65,"Description":"Description for Product 9"},{"id":72,"ArticleNo":4876386493,"Product":"Product 10","inPrice":54156,"Price":1706394,"Unit":"Piece","inStock":89,"Description":"Description for Product 10"},{"id":73,"ArticleNo":2800441092,"Product":"Product 11","inPrice":12397,"Price":1400929,"Unit":"Kg","inStock":54,"Description":"Description for Product 11"},{"id":74,"ArticleNo":9200764438,"Product":"Product 12","inPrice":1280,"Price":524818,"Unit":"Kg","inStock":70,"Description":"Description for Product 12"},{"id":75,"ArticleNo":9619323085,"Product":"Product 13","inPrice":85612,"Price":1187133,"Unit":"Kg","inStock":69,"Description":"Description for Product 13"},{"id":76,"ArticleNo":9080206171,"Product":"Product 14","inPrice":65100,"Price":460234,"Unit":"Piece","inStock":25,"Description":"Description for Product 14"},{"id":77,"ArticleNo":6699514855,"Product":"Product 15","inPrice":81104,"Price":1044044,"Unit":"Kg","inStock":11,"Description":"Description for Product 15"},{"id":78,"ArticleNo":9272130698,"Product":"Product 16","inPrice":12225,"Price":462301,"Unit":"Piece","inStock":19,"Description":"Description for Product 16"},{"id":79,"ArticleNo":2571472752,"Product":"Product 17","inPrice":7019,"Price":1380450,"Unit":"Kg","inStock":15,"Description":"Description for Product 17"},{"id":80,"ArticleNo":8620922048,"Product":"Product 18","inPrice":55420,"Price":1840476,"Unit":"Liter","inStock":9,"Description":"Description for Product 18"},{"id":81,"ArticleNo":4521660667,"Product":"Product 19","inPrice":85446,"Price":740732,"Unit":"Piece","inStock":1,"Description":"Description for Product 19"},{"id":82,"ArticleNo":7853266096,"Product":"Product 20","inPrice":92019,"Price":1027648,"Unit":"Liter","inStock":47,"Description":"Description for Product 20"}]
    converted_list = [
            [product["ArticleNo"], product["Product"], product["inPrice"], product["Price"],
            product["Unit"], product["inStock"], product["Description"]]
            for product in data
        ]
    return {"message": converted_list}