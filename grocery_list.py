from fastapi import FastAPI, HTTPException


app = FastAPI()

grocery_list = [
    {"item" : "bread", "qty" : 1},
    {"item" : "milk", "qty" : 2}
]

@app.post('/create', status_code=201)
async def add_item(item : dict):
    for temp_item in grocery_list:
        if temp_item['item'] == item['item']:
            raise HTTPException(status_code=400, detail= f"{item['item']} already present!")

    grocery_list.append(item)
    
    return {"data" : f"{item['item']} added correctly!"}

@app.get('/list', status_code=200)
async def get_list():
    return {"data":grocery_list}

@app.put('/update', status_code=200)
async def update_item(item_name:str, item_quantity:int):
    for temp_item in grocery_list:
        if temp_item['item'] == item_name:
            temp_item['qty'] = item_quantity
            return {"data" : f"{item_name} correctly updated!"}

    raise HTTPException(status_code=404, detail=f"{item_name} not found!")

@app.delete('/delete/{item_name}',status_code=200)
async def delete_item(item_name:str):
    for temp_item in grocery_list:
        if temp_item['item'] == item_name:
            grocery_list.remove(temp_item)
            return {"data" : f"{item_name} correctly deleted!"}

    raise HTTPException(status_code=404, detail=f"{item_name} not found!")

if __name__ == '__main__':

    app.run(port=5000, reload=True)