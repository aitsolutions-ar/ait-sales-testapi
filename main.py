from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from helper import products

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)


@app.get("/products")
async def list_products():
    return {"products": products}


@app.post("/sales/", status_code=status.HTTP_201_CREATED)
async def create_sale():
    return {"message": "created"}
