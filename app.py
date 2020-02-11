from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [

{
    "name": "Apple Store",
    "items": [
        {
            "name": "iPhone",
            "price": 399
        }
    ]
}

]


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def createStore():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)



# GET /store/<string:name>
@app.route('/store/<string:name>')
def getStore(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
        else:
            return jsonify({"message": "Store not found"})
        


# GET /store
@app.route('/store')
def getStores():
    return jsonify({'stores': stores})



# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def createStoreItems(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "store not found"})        

    



# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def getItemInStore(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
        else:
            return jsonify({"message": "Store not found"})


app.run(port=5000)