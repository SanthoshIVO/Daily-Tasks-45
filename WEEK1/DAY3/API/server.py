from fastapi import FastAPI, HTTPException
from mockData import products
from productDTO import product_DTO

app = FastAPI()



@app.get("/")
def homw():
    return {"message": "Welcome to the Product API"}

@app.get("/products")
def get_products():
    return products
#path parameter
@app.get("/products/{product_id}")
def get_one_product(product_id: int):
    for oneProduct in products:
        print("error", oneProduct, product_id)
        if oneProduct.get("id") == product_id:
            return oneProduct

    raise HTTPException(
        status_code=404,
        detail=f"Product with ID {id} is not available",
    )

#query parameter
@app.get("/products/search")
def search_product(name: str):
    for oneProduct in products:
        if oneProduct.get("name") == name:
            return oneProduct

    raise HTTPException(
        status_code=404,
        detail=f"Product with name {name} is not available",
    )

#body, headers, - request heasers, query params

#diff types of http methods


@app.post("/create_products")
def send_data(product: product_DTO):
   
    product = product.model_dump()
    
    products.append(product)
    

    return {
        "message": "data is saved to memory successfully",
        "data": products
    }


@app.put("/update_product/{product_id}")
def update_product(product_id: int, product: product_DTO):

    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product.model_dump()
            return {
                "message": f"Product with ID {product_id} has been updated",
                "updated_product": products[index]
            }

    raise {
        
        "error": f"Product with ID {product_id} is not available"
    }


@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {
                "message": f"Product with ID {product_id} has been deleted",
                "deleted_product": deleted_product
            }

    raise {

        "error":f"Product with ID {product_id} is not available"
    }